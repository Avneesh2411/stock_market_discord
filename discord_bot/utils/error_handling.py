```python
import logging

def log_error(error):
    logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)
    logging.error(f'Error occurred: {error}')

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_error(e)
    return wrapper
```