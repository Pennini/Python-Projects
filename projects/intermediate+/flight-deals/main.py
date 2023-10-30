from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

data = DataManager()
fg_data = FlightData()

sheet_data = data.get_data()

for dt in sheet_data:
    dt = fg_data.get_iata(dt)
    suc = data.update_table(dt)

pprint(sheet_data)
