from abc import ABC
from typing import Type, List

from pydantic import BaseModel

from db_utils.session_container import SessionContainer


class BaseRepo(ABC):
    def __init__(self, collection_name: str, base_type):
        self.base_type = base_type
        self.collection_name = collection_name

    def get_all(self):
        session = SessionContainer.get_session()
        bids_collection = session[self.collection_name]
        existing_bids_documents = bids_collection.find({})
        existing_bids: List[Type] = [self.base_type(**bid_doc) for bid_doc in existing_bids_documents]
        a = existing_bids
