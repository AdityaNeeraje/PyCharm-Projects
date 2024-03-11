from datetime import datetime, timedelta
import pandas
from pandas_datareader import data
from os import environ

tickers = ['AAPL', 'MSFT']
start_date = (datetime.today() - timedelta(days=8)).strftime("%Y-%m-%d")
end_date = datetime.today().strftime("%Y-%m-%d")
# QUANDL_API_KEY = environ.get("QUANDL_API_KEY")
IEX_API_KEY = environ.get("IEX_API_KEY")
panel_data = data.DataReader('F', 'iex', start_date, end_date)
print(panel_data.head(8))


# import requests
# from os import environ
# from langdetect import detect
# from langdetect.lang_detect_exception import LangDetectException
# import smtplib
# from time import sleep
#
# def is_english(text):
#     try:
#         if detect(text) == "en":
#             return True
#         else:
#             return False
#     except LangDetectException:
#         return False
#
#
# stocks_to_follow = {"Tesla": "TSLA", "Visa": "VISA", "Nvidia": "NVDA", "Google": "GOOG", "Apple": "AAPL", "Mastercard": "MA"}
# url = "https://www.alphavantage.co/query"
# news_url = "https://newsapi.org/v2/top-headlines"
#
# API_KEY = environ.get("API_KEY")
# news_apikey = environ.get("NEWS_API_KEY")
# email_address = environ.get("EMAIL_ADDRESS")
# app_password = environ.get("APP_PASSWORD")
#
# # params = {
# #     "apiKey": news_apikey,
# #     "q": "Nvidia",
# # }
# # response = requests.get(news_url, params=params).json()
# #
# # for stock in stocks_to_follow:
# #     params = {
# #         "apiKey": news_apikey,
# #         "q": stock.title()
# #     }
# #     response = requests.get(news_url, params=params).json()
# #     print(response)
# #     if response['status'] == "ok" and response['articles']:
# #         response = [article for article in response['articles'] if is_english(article['title']) and is_english(article['description'])]
# #         if len(response) > 3:
# #             response = response[:3]
# #         response = [f"{article['source']['name']}: {article['title']}\n{article['description']}\n{article['url']}\n\n" for article in response]
# #         for attempt in range(5):
# #             try:
# #                 with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
# #                     connection.starttls()
# #                     connection.login(user=email_address, password=app_password)
# #                     connection.sendmail(to_addrs=email_address, from_addr=email_address, msg=f"Subject: {stock.title()} shares rose by 5% today!\n\n{stock.title()} stocks {'rose'} by {'5'}% yesterday. Here are some relevant news articles regarding {stock.title()}'s activities from yesterday.\n{''.join(response)}".encode('utf-8'))
# #                     break
# #             except (ConnectionError, ConnectionRefusedError, TimeoutError) as error:
# #                 print(error)
# #                 sleep(5)
# #     else:
# #         print(response)
#
# # params = {"function": "TIME_SERIES_DAILY", "symbol": "TESLA", "apikey": API_KEY}
# # headers = {"apikey": API_KEY}
#
# for stock in stocks_to_follow:
#     response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}").json()
#     print(response)
#     if response.get("Time Series (Daily)") is not None:
#         seven_day_closing_prices = [float(list(response["Time Series (Daily)"].values())[index]["4. close"]) for index in range(7)]
#         current_price = seven_day_closing_prices[0]
#         last_price = seven_day_closing_prices[1]
#         seven_day_moving_average = sum(seven_day_closing_prices)/len(seven_day_closing_prices)
#         print(100*abs((current_price - last_price)/last_price))
#         if 100*abs((current_price - last_price)/last_price) >= 5:
#             if current_price > last_price:
#                 change_direction = "rose"
#             else:
#                 change_direction = "fell"
#
#
#     # print(pandas.read_csv(response.json()))
