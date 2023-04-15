import requests
from datetime import datetime as dt
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

API_KEY = os.environ.get("API_KEY")
STOCK_URL = "https://www.alphavantage.co/query"
params = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK, "interval": "5min", "apikey": API_KEY}


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
    return abs(yesterday.close - the_day_before_yesterday.close) / the_day_before_yesterday.close


response = requests.get(STOCK_URL, params=params)
time_series_dict = response.json().get("Time Series (Daily)")
yesterday_data, the_day_before_yesterday_data = get_the_last_two_days_from(time_series_dict)

if calculate_difference(yesterday=yesterday_data, the_day_before_yesterday=the_day_before_yesterday_data) > 0.05:
    print("Get News")

# TODO 2
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# TODO 3
# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


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
