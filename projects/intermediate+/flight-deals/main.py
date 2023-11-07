from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

ORIGIN_CITY_IATA = "GRU"

data = DataManager()
fg_search = FlightSearch()
notification = NotificationManager()

sheet_data = data.get_data()

date_from = dt.datetime.now() + dt.timedelta(30)
date_to = date_from + dt.timedelta(6 * 30)

emails = data.get_emails()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = fg_search.get_iata(row)
        data.update_table(row)
    fg_data = fg_search.get_price(row, ORIGIN_CITY_IATA, date_from, date_to)
    if fg_data:
        notification.send_emails(fg_data, emails)
        # notification.send_sms(fg_data)

