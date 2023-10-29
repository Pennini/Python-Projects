import requests
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv(r'../../../.env')

headers = {
    'key': os.getenv('NUTRITION_KEY'),
    'id': os.getenv('NUTRITION_ID')
}
print(headers)




