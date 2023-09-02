from typing import List
from pymongo import MongoClient
from bid_helper import BidHelper
from models import Bid, SavedBid
from rami_client import RamiClient


result = []
new_rami_data = RamiClient.call_rami()
new_bids_data: List[Bid] = BidHelper.convert_rami_data_to_bids(new_rami_data)

client = MongoClient("mongodb://127.0.0.1:27017")
bids_db = client.bids_db
bids_collection = bids_db.bids
print("Connection Successful")

existing_bids_documents = bids_collection.find({})
existing_bids: List[SavedBid] = [SavedBid(**bid_doc) for bid_doc in existing_bids_documents]


def save_new_bid(new_bid_data: Bid):
    bids_collection.insert_one(new_bid_data.__dict__)


def update_bid(existing_bid: SavedBid, new_bid_data: Bid):
    bids_collection.update_one({"_id": str(existing_bid.id)}, {"$set": new_bid_data.__dict__})


for new_bid_data in new_bids_data:
    existing_bid = next((existing_bid for existing_bid in existing_bids if existing_bid.bid_id == new_bid_data.bid_id),
                        None)
    if existing_bid:
        if new_bid_data.equals(existing_bid):
            print("No need to update")
        else:
            update_bid(existing_bid, new_bid_data)
    else:
        save_new_bid(new_bid_data)

    # Query existing from DB (Mongo)?
    #       Downloaded $ brew cask install gcollazo-mongodb
    #       Created /via/data/db
    #       mongod --dbpath=/via/data/db - to run mongo
    #       mongosh "mongodb://localhost:27017"
    #       Downloaded shell from https://www.mongodb.com/try/download/shell
    #       Moved its been to the same pass of the gcollazo-mongodb that were added to the PATH
    # Compare - V
    # Run in docker
    # Notify in SMS on new bids
    # Run on server periodically (K8S)
    # Test
    # Subscribe / Unsubscribe
client.close()
len(result)

#       mongod --dbpath=/via/data/db - to run mongo
#       mongosh "mongodb://localhost:27017"

# db.bids.updateOne({"_id": "64f379d4569c2b055d17d0b2"}, {$set:{
#     bid_id: 20230212,
#     city: '',
#     bid_status: 1,
#     bid_book_published: false,
#     is_online_bid: true,
#     number_of_units: 3,
#     publish_date: '2023-08-20T00:00:00+03:00',
#     opening_date: '2023-09-25T00:00:00+03:00',
#     closing_date: '2023-11-27T12:00:00+02:00',
#     committee_date: null,
#     designated_public: 1,
#     bid_book_last_update_date: null
#   }})
