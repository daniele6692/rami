from functools import cache

from pymongo import MongoClient
from src.utils.env_utils import get_env_var

@cache
class DbClient(object):
    _db_client = None

    def __init__(self):
        print("Created DB Client")
        self._db_client = self._init_db_client()

    def get_session(self):
        return self._db_client.bids_db

    def _init_db_client(self):
        host = get_env_var('MONGO_HOST')
        if not host:
            raise Exception("Missing DB Host")
        user = get_env_var('MONGO_INITDB_ROOT_USERNAME')
        password = get_env_var('MONGO_INITDB_ROOT_PASSWORD')
        creds_string = ""
        if user and password:
            creds_string = f'{user}:{password}@'
        mongo_url = f'mongodb://{creds_string}{host}:27017/'
        print(f"MONGO_URL is {mongo_url}")
        return MongoClient(mongo_url)


