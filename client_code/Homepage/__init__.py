from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EntryEdit import EntryEdit
from datetime import date
# import threading

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.item['date'] = date.today().isoformat()
    r = app_tables.pushups.get(date=date.today().isoformat())
    self.item['today_count'] = r['count'] if r else 0
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    entries = anvil.server.call('get_entries')
    self.bar_chart.data = go.Bar(x=entries['dates'], y=entries['counts'])
    # threading.Timer(2, form_refreshing_data_bindings).start()

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    print("Refresh data binding")
    self.item['date'] = date.today().isoformat()
    r = app_tables.pushups.get(date=date.today().isoformat())
    self.item['today_count'] = r['count'] if r else 0
    entries = anvil.server.call('get_entries')
    self.bar_chart.data = go.Bar(x=entries['dates'], y=entries['counts'])
    self.refresh_data_bindings()

