import pymongo

from src.db_utils.db_client import db_client


class SessionContainer():
    @staticmethod
    def get_session() -> pymongo.database.Database:
        bids_db = db_client.bids_db
        return bids_db

    @staticmethod
    def close_session():
        db_client.close()
