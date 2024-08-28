from src.db_utils.db_client import DbClient


class SessionContainer(object):
    db_client: DbClient = None

    @classmethod
    def init_session(cls):
        cls.db_client = DbClient()

    @classmethod
    def get_session(cls):
        return cls.db_client.get_session()
