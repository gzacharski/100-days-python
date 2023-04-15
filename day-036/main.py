import random
import requests
from datetime import datetime as dt
import os
from twilio.rest import Client as TwilioClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#  Run before
#  export TWILIO_ACCOUNT_SID=<change_me>;
#  export TWILIO_AUTH_TOKEN=<change_me>;
#  export TWILIO_FROM_NUMBER=<change_me>;
#  export TWILIO_TO_NUMBER=<change_me>;
#  export STOCK_API_KEY=<change_me>;
#  export NEWS_API_KEY=<change_me>;


TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_FROM_NUMBER = os.environ["TWILIO_FROM_NUMBER"]
TWILIO_TO_NUMBER = os.environ["TWILIO_TO_NUMBER"]

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_PARAMS = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK, "interval": "5min", "apikey": STOCK_API_KEY}

NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMS = {"qInTitle": COMPANY_NAME, "apiKey": NEWS_API_KEY}


class DailyStockData:
    def __init__(self, date_and_time: str, data: dict):
        self.date = dt.fromisoformat(date_and_time).date()
        self.open = float(data.get("1. open"))
        self.close = float(data.get("4. close"))


def get_the_last_two_days_from(time_series: dict) -> (DailyStockData, DailyStockData):
    keys = time_series.keys()
    two_last_days = list(keys)[:2]

    def to_daily_stock_data(date_and_time: str) -> DailyStockData:
        daily_stock_data_dict = time_series.get(date_and_time)
        return DailyStockData(date_and_time, daily_stock_data_dict)

    daily_stock_data_list = [to_daily_stock_data(date_and_time) for date_and_time in two_last_days]
    return tuple(daily_stock_data_list)


def calculate_difference(yesterday: DailyStockData, the_day_before_yesterday: DailyStockData):
    return (yesterday.close - the_day_before_yesterday.close) / the_day_before_yesterday.close


response = requests.get(STOCK_URL, params=STOCK_PARAMS)
time_series_dict = response.json().get("Time Series (Daily)")
yesterday_data, the_day_before_yesterday_data = get_the_last_two_days_from(time_series_dict)

difference = calculate_difference(yesterday=yesterday_data, the_day_before_yesterday=the_day_before_yesterday_data)
if abs(difference) > 0.001:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    response = requests.get(NEWS_URL, params=NEWS_PARAMS)
    articles = response.json().get("articles")[:3]

    # TODO 3
    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.

    chosen_article = random.choice(articles)

    body = f"""
        TSLA:  {"🔺" if difference > 0 else "🔻"}{abs(difference)}%
        Headline: {chosen_article.get("title")}. 
        Brief: {chosen_article.get("description")}.
        """

    client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=TWILIO_FROM_NUMBER,
        to=TWILIO_TO_NUMBER
    )
