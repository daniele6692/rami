from pymongo import MongoClient

db_client = MongoClient("mongodb://127.0.0.1:27017")
print("Connection Successful")