import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, date
# import pandas as pd
# import numpy as np
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
  # df_dict = {
  #   'Date': [],
  #   'Count': []
  # }
  entries = {
    'counts': [],
    'dates': []
  }
  data = app_tables.pushups.search()
  for entry in data:
    entries['dates'].append(entry['date'])
    entries['counts'].append(entry['count'])

  # Convert dictionary to DataFrame
  # df = pd.DataFrame(df_dict)
  # df['Date'] = pd.to_datetime(df['Date'])
  # print(df.head())
  return entries

