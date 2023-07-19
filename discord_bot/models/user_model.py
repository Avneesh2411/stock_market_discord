```python
class User:
    def __init__(self, id, username, stocks):
        self.id = id
        self.username = username
        self.stocks = stocks

    def add_stock(self, stock):
        if stock not in self.stocks:
            self.stocks.append(stock)

    def remove_stock(self, stock):
        if stock in self.stocks:
            self.stocks.remove(stock)

    def get_stocks(self):
        return self.stocks
```