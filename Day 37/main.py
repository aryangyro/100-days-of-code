import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_KEY = os.environ.get("alpha_key")
NEWS_KEY = os.environ.get("news_key")

# -------------------- STEP 1: STOCK DATA -------------------- #

stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_KEY
}

stock_response = requests.get(stock_url, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()

if "Time Series (Daily)" not in stock_data:
    print("Alpha Vantage error:")
    print(stock_data)
    exit()

data = stock_data["Time Series (Daily)"]

data_list = list(data.values())

yesterday_close = float(data_list[0]["4. close"])
day_before_close = float(data_list[1]["4. close"])

difference = yesterday_close - day_before_close
percent_change = round((difference / day_before_close) * 100, 2)

# Emoji indicator
if percent_change > 0:
    direction = "🔺"
else:
    direction = "🔻"

# -------------------- STEP 2: NEWS -------------------- #

if abs(percent_change) >= 5:
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 3
    }

    news_response = requests.get(news_url, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    # -------------------- STEP 3: SMS -------------------- #

    client = Client(
        os.environ.get("sid"),
        os.environ.get("auth")
    )

    for article in articles:
        message_body = (
            f"{STOCK}: {direction}{abs(percent_change)}%\n"
            f"Headline: {article['title']}\n"
            f"Brief: {article['description']}"
        )

        client.messages.create(
            body=message_body,
            from_=os.environ.get("tnum"),
            to=os.environ.get("mnum")
        )