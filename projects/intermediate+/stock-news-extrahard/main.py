STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import sys
import requests
import datetime as dt
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv("../../../.env")


caminho_diretorio = r"C:\Users\Lenovo\Desktop\FEA DEV\fin_quant\curso"
sys.path.append(caminho_diretorio)

from secrets_api import ALPHA_VANTAGE_API_TOKEN, NEWS_API_KEY, AUTH_TOKEN

account_sid = os.getenv("TWILIO_SID")
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock(stock: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={ALPHA_VANTAGE_API_TOKEN}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    yesterday = str(dt.datetime.now() - dt.timedelta(days=1))[:10]
    before_yesterday = str(dt.datetime.now() - dt.timedelta(days=2))[:10]

    try:
        yesterday_price = float(data[yesterday]["4. close"])
        before_yesterday_price = float(data[before_yesterday]["4. close"])
    except TypeError:
        print("Must be a number")
        return
    except Exception as mes:
        print(f"Error getting stock price\n{mes}")
        return

    percentage = round(
        ((yesterday_price - before_yesterday_price) / before_yesterday_price) * 100, 2
    )
    if percentage < -5 or percentage > 5:
        return True, percentage
    else:
        return False, percentage


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&from=2023-09-05&sortBy=publishedAt&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    response.raise_for_status()
    return response.json()["articles"][:3]


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_sms(percentage, news):
    if percentage > 0:
        arrow = "🔺"
    else:
        arrow = "🔻"
    for info in news:
        message = client.messages.create(
            from_="+12315359834",
            body=f"TSLA: {arrow}{percentage}%\nHeadline: {info['title']}\nBrief: {info['description']}",
            to="+5511999001064",
        )
        print(message.sid)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

result, percentage = get_stock(STOCK)
if result:
    data = get_news(COMPANY_NAME)
    send_sms(percentage, data)
