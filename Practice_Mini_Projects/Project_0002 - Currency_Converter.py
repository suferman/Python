import requests
import pandas as pd

API_KEY = "api_key" #get your API from https://app.freecurrencyapi.com/dashboard
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}" #

CURRENCIES = ["USD", "CAD", "EUR", "JPY", "CNY"] #list of currencies needed

def convert_currency(base):
    currencies = ",".join(CURRENCIES) #convert CURRENCIES to comma-separated values, which is the string expected by this function
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}" #specify needed data
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except:
        print("We don't have data for that. Sorry!")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()
    if base == "Q":
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

#Credits
# Project based on a tutorial by [Tech With Tim]
# YouTube channel: [https://www.youtube.com/@TechWithTim]
# Original video: [https://www.youtube.com/watch?v=zT7niRUOs9o&list=PLr2Clb5apOx1WXe_eIAW9PbcDP9GVacv_&index=6]
