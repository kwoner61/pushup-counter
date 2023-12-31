from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EntryEdit import EntryEdit
from datetime import date


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    d = date.today().isoformat()
    self.item['date'] = d
    r = app_tables.pushups.get(date=d)
    self.item['today_count'] = r['count'] if r else 0
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    entries = anvil.server.call_s('get_entries')
    self.bar_chart.data = go.Bar(x=entries['dates'], y=entries['counts'])


  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    d = date.today().isoformat()
    self.item['date'] = d
    r = app_tables.pushups.get(date=d)
    self.item['today_count'] = r['count'] if r else 0
    entries = anvil.server.call_s('get_entries')
    self.bar_chart.data = go.Bar(x=entries['dates'], y=entries['counts'])
    self.refresh_data_bindings()


  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.form_refreshing_data_bindings()

