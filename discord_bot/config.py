import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')