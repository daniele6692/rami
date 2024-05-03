import os

from pymongo import MongoClient

user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
password = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
mongo_uri = os.getenv('MONGO_URI')
if user and password:
    MONGO_URL = f'mongodb://{user}:{password}@mongodb:27017'
elif mongo_uri:
    MONGO_URL = mongo_uri
else:
    MONGO_URL = 'mongodb://127.0.0.1:27017'
print(f"MONGO_URL is {MONGO_URL}")
db_client = MongoClient(MONGO_URL)
print("Connection Successful")