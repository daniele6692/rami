from abc import ABC
from typing import List, Type, TypeVar

from src.db_utils.session_container import SessionContainer

T = TypeVar("T")


class BaseRepo(ABC):
    def __init__(self, collection_name: str, base_type: T):
        self.base_type = base_type
        self.collection_name = collection_name

    def get_all(self, filter: dict = None) -> List[T]:
        collection = self.get_collection()
        existing_records = collection.find(filter)
        existing_bids: List[Type] = [
            self.base_type(**record) for record in existing_records
        ]
        return existing_bids

    def get_collection(self):
        session = SessionContainer().get_session()
        collection = session[self.collection_name]
        return collection

    def update(self, existing_record: T, new_data: dict):
        collection = self.get_collection()
        collection.update_one({"_id": existing_record.id}, {"$set": new_data})

    def save(self, new_entity: T):
        collection = self.get_collection()
        collection.insert_one(new_entity.__dict__)

    def delete(self, deletion_criteria):
        collection = self.get_collection()
        collection.delete_many(deletion_criteria)
