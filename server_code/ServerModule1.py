import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, date


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
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.entries.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def update_entry(entry, entry_dict):
  # check that the entry given is really a row in the ‘entries’ table
  if app_tables.entries.has_row(entry):
    entry_dict['updated'] = datetime.now()
    entry.update(**entry_dict)
  else:
    raise Exception("Entry does not exist")

@anvil.server.callable
def delete_entry(entry):
  # check that the entry being deleted exists in the Data Table
  if app_tables.entries.has_row(entry):
    entry.delete()
  else:
    raise Exception("Entry does not exist")