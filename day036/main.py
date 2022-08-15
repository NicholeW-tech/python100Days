import requests

from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TSLA_API_KEY = #key
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = #accountsid
auth_token = #auth_token



parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey": TSLA_API_KEY,
}

parameters2 = {
    "q": "tesla",
    "from":"2022-01-03",
    "sort_by": "publishedAt",
    "apiKey": #key,


}

url = 'https://www.alphavantage.co/query'
r = requests.get(url=url, params=parameters)
r.raise_for_status()
data = r.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]
yesterday_closing_price = data_list[0]['4. close']
day_before_closing_price = data_list[1]['4. close']
# today = datetime.now().date()
# yesterday = str(today - timedelta(days = 1))
# day_before_yesterday = str(today - timedelta(days = 2))
# yesterday_close = data['Time Series (Daily)'][yesterday]['4. close']
# day_before_yesterday_close = data['Time Series (Daily)'][day_before_yesterday]['4. close']
# print(yesterday_close)
# print(day_before_yesterday_close)
percentage_diff = (round(float(yesterday_closing_price) - float(day_before_closing_price)) / float(yesterday_closing_price) * 100)
up_down = None
if percentage_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


if abs(percentage_diff) > 5:
    request = requests.get(url="https://newsapi.org/v2/everything", params=parameters2)
    request.raise_for_status()
    news_data = request.json()
    article_list = news_data["articles"][0:3]
    formatted_articles = [f"{STOCK_NAME:{up_down}{percentage_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in article_list]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
        .create(
        body= article,
        from_='sender #',
        to='your #'
        )
