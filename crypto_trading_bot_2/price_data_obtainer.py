import pandas as pd
import requests
import datetime
import yaml
from yaml.loader import SafeLoader

keys = yaml.load(f, Loader=SafeLoader)
url = keys['url']

bitcoin_chart_request = requests.get(url, verify=False)
bitcoin_chart_json = bitcoin_chart_request.json()

print(bitcoin_chart_json)
time = datetime.datetime.fromtimestamp(bitcoin_chart_json[0][0]).strftime('%c')
print(time)

bitcoin_chart_clean = []
for day in bitcoin_chart_json:
    day[0] = datetime.datetime.fromtimestamp(day[0]).strftime('%c')
    bitcoin_chart_clean.append(day[0:6])
df = pd.DataFrame(
    data=bitcoin_chart_clean,
    columns=[
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"]
    )

df.to_csv("crypto_trading_bot_2/pricedata.csv", index=False)