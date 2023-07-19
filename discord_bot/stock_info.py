```python
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

def get_stock_info(company_name):
    base_url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY"
    symbol = company_name
    datatype = "json"
    api_key = STOCK_API_KEY

    data = {
        "function": function,
        "symbol": symbol,
        "datatype": datatype,
        "apikey": api_key
    }

    response = requests.get(base_url, params=data)
    response_json = response.json()

    df = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient='index')
    df = df.sort_index(axis=1)

    return df
```