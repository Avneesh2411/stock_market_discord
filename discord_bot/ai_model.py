```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from discord_bot.utils import data_processing
from discord_bot.models import stock_data_model

class StockPredictor:
    def __init__(self, stock_data):
        self.stock_data = stock_data
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(LSTM(128, input_shape=(self.stock_data.train_X.shape[1:]), return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(128, return_sequences=True))
        model.add(Dropout(0.1))
        model.add(LSTM(128))
        model.add(Dropout(0.2))
        model.add(Dense(32, activation='relu'))
        model.add(Dropout(0.2))
        model.add(Dense(10, activation='softmax'))

        opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)
        model.compile(loss='sparse_categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

        return model

    def train_model(self):
        self.model.fit(self.stock_data.train_X, self.stock_data.train_y, epochs=3, validation_data=(self.stock_data.validation_X, self.stock_data.validation_y))

    def predict_stock(self, stock_data):
        prediction = self.model.predict(stock_data)
        return prediction
```