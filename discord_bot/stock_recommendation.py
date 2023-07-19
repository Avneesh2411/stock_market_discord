```python
import os
import requests
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler

load_dotenv()
STOCK_API_KEY = os.getenv('STOCK_API_KEY')

def get_historical_data(symbol):
    base_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={STOCK_API_KEY}"
    response = requests.get(base_url)
    data = response.json()
    df = pd.DataFrame(data['Time Series (Daily)']).T
    df = df['4. close'].astype(float)
    return df

def create_model():
    model = Sequential()
    model.add(LSTM(50, return_sequences=True))
    model.add(LSTM(50, return_sequences=False))
    model.add(Dense(25))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def recommend_stocks():
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']
    predictions = {}

    for symbol in symbols:
        data = get_historical_data(symbol)
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(data.values.reshape(-1,1))

        model = create_model()
        model.fit(scaled_data[:-60], scaled_data[60:], batch_size=1, epochs=1)

        last_60_days = scaled_data[-60:]
        last_60_days = np.reshape(last_60_days, (1, last_60_days.shape[0], 1))
        prediction = model.predict(last_60_days)
        prediction = scaler.inverse_transform(prediction)

        predictions[symbol] = prediction[0][0]

    recommended_stock = max(predictions, key=predictions.get)
    return recommended_stock
```