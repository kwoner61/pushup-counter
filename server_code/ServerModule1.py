import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, date
import plotly.graph_objects as go


@anvil.server.callable
def add_entry():
  d = date.today().isoformat()
  r = app_tables.pushups.get(date=d)
  if r:
    entry_dict = {}
    entry_dict['count'] = r['count'] + 1
    entry_dict['updated'] = datetime.now()
    r.update(**entry_dict)
  else:
    app_tables.pushups.add_row(count=1, date=d, created=datetime.now())


@anvil.server.callable
def get_entries():
  entries = {
    'counts': [],
    'dates': []
  }
  data = app_tables.pushups.search()
  for entry in data:
    entries['dates'].append(entry['date'])
    entries['counts'].append(entry['count'])
  return entries
