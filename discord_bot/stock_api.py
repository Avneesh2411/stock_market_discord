```python
import requests
import pandas as pd
from .config import STOCK_API_KEY
from .utils import data_processing

class StockAPI:
    def __init__(self):
        self.base_url = "https://api.example.com"  # Replace with your stock API base URL
        self.api_key = STOCK_API_KEY

    def fetch_stock_data(self, symbol):
        endpoint = f"{self.base_url}/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(endpoint)
        data = response.json()

        if "Error Message" in data:
            return None

        stock_data = data["Time Series (Daily)"]
        processed_data = data_processing.process_stock_data(stock_data)

        return processed_data

    def fetch_multiple_stocks_data(self, symbols):
        stocks_data = {}

        for symbol in symbols:
            stock_data = self.fetch_stock_data(symbol)
            if stock_data is not None:
                stocks_data[symbol] = stock_data

        return stocks_data
```