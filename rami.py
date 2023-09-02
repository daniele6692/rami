import uuid

import requests
from typing import Optional
from pydantic import BaseModel, Field, AliasChoices
from pymongo import MongoClient

from const import open_bids_in_center_and_tel_aviv, Villeges, city_code_field_name, audience_code_field_name, \
    designated_for_the_public_codes, bid_preference_code_field_name, no_preference_codes


class Bid(BaseModel):
    bid_id: int = Field(validation_alias=AliasChoices("MichrazID", "bid_id"))
    city: str
    bid_status: int = Field(validation_alias=AliasChoices("StatusMichraz", "bid_status"))
    bid_book_published: bool = Field(validation_alias=AliasChoices("PublishedChoveret", "bid_book_published"))
    is_online_bid: bool = Field(validation_alias=AliasChoices("Mekuvan", "is_online_bid"))
    number_of_units: int = Field(validation_alias=AliasChoices("YechidotDiur", "number_of_units"))
    publish_date: Optional[str] = Field(validation_alias=AliasChoices("PirsumDate", "publish_date"))
    opening_date: Optional[str] = Field(validation_alias=AliasChoices("PtichaDate", "opening_date"))
    closing_date: Optional[str] = Field(validation_alias=AliasChoices("SgiraDate", "closing_date"))
    committee_date: Optional[str] = Field(validation_alias=AliasChoices("VaadaDate", "committee_date"))
    designated_public: Optional[int] = Field(validation_alias=AliasChoices("KhalYaadRashi", "designated_public"))
    bid_book_last_update_date: Optional[str] = Field(validation_alias=AliasChoices("ChoveretUpdateDate", "bid_book_last_update_date"))

    def equals(self, other_bid):
        if type(other_bid) != Bid or other_bid != dict:
            return False
        if type(other_bid) == Bid:
            other_bid = other_bid.__dict__
        other_bid_values = other_bid.pop("id", None)
        current_bid_values = self.__dict__.pop("id", None)
        return all(other_bid_values[key] == current_bid_values[key] for key in other_bid_values.keys())

response = requests.post('https://apps.land.gov.il/MichrazimSite/api/SearchApi/Search',
                         json=open_bids_in_center_and_tel_aviv)

bids = response.json()
result = []
client = MongoClient("mongodb://127.0.0.1:27017")
bids_db = client.bids_db
bids_collection = bids_db.bids
print("Connection Successful")

existing_bids_documents = bids_collection.find({})
existing_bids = [Bid(**bid_doc) for bid_doc in existing_bids_documents]


for bid in bids:


    city_name = Villeges.get(bid.get(city_code_field_name))
    audience_code = bid.get(audience_code_field_name)
    bid_preference_code = bid.get(bid_preference_code_field_name)
    is_bid_with_preference = bid_preference_code in no_preference_codes
    for_private_structure = audience_code in designated_for_the_public_codes
    bid_with_city_name = {**bid, "city": city_name, "for_private_structure": for_private_structure,
                          "is_bid_with_preference": is_bid_with_preference}
    print(bid_with_city_name)
    current_bid = Bid(**bid_with_city_name)
    a = current_bid.__dict__
    saved_bid = bids_collection.insert_one(a)
    bids_collection.find_one(saved_bid.inserted_id)

    # Query existing from DB (Mongo)?
    #       Downloaded $ brew cask install gcollazo-mongodb
    #       Created /via/data/db
    #       mongod --dbpath=/via/data/db - to run mongo
    #       mongosh "mongodb://localhost:27017" -
    #       Downloaded shell from https://www.mongodb.com/try/download/shell
    #       Moved its been to the same pass of the gcollazo-mongodb that were added to the PATH
    # Compare
    # Run in docker
    # Notify in SMS on new bids
    # Run on server periodically (K8S)
    # Test
    # Subscribe / Unsubscribe
    result.append(current_bid)
client.close()
len(result)
