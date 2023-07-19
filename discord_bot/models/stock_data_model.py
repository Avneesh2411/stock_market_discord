```python
class StockData:
    def __init__(self, symbol, company_name, latest_price, change_percent, market_cap, pe_ratio):
        self.symbol = symbol
        self.company_name = company_name
        self.latest_price = latest_price
        self.change_percent = change_percent
        self.market_cap = market_cap
        self.pe_ratio = pe_ratio

    def to_dict(self):
        return {
            'symbol': self.symbol,
            'company_name': self.company_name,
            'latest_price': self.latest_price,
            'change_percent': self.change_percent,
            'market_cap': self.market_cap,
            'pe_ratio': self.pe_ratio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['symbol'],
            data['company_name'],
            data['latest_price'],
            data['change_percent'],
            data['market_cap'],
            data['pe_ratio']
        )
```