```python
import pandas as pd
import numpy as np

def process_raw_data(raw_data):
    try:
        data_frame = pd.DataFrame(raw_data)
        data_frame = data_frame.dropna()  # remove missing values
        data_frame = data_frame.astype(float)  # convert all values to float
        return data_frame
    except Exception as e:
        raise e

def normalize_data(data_frame):
    try:
        normalized_df=(data_frame-data_frame.min())/(data_frame.max()-data_frame.min())
        return normalized_df
    except Exception as e:
        raise e

def split_data(data_frame, train_ratio=0.8):
    try:
        train_size = int(len(data_frame) * train_ratio)
        train, test = data_frame[0:train_size], data_frame[train_size:len(data_frame)]
        return train, test
    except Exception as e:
        raise e

def create_dataset(dataset, look_back=1):
    try:
        dataX, dataY = [], []
        for i in range(len(dataset)-look_back-1):
            a = dataset[i:(i+look_back), 0]
            dataX.append(a)
            dataY.append(dataset[i + look_back, 0])
        return np.array(dataX), np.array(dataY)
    except Exception as e:
        raise e
```