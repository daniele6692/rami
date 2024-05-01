import os

from pymongo import MongoClient

MONGO_URL = os.getenv('MONGO_URL')
print(f"MONGO_URL is {MONGO_URL}")
db_client = MongoClient(MONGO_URL)
print("Connection Successful")