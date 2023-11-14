from typing import List

from bid_helper import BidHelper
from db_utils.session_container import SessionContainer
from models.bid_update_result import BidsUpdateResult
from models.bids import SavedBid, Bid
from rami_client import RamiClient
from reops.bid_repo import BidRepo


b = BidRepo()
b.get_all()
bids_update_result = BidsUpdateResult()

raw_bids = RamiClient.get_raw_bids()
new_bids_data: List[Bid] = BidHelper.convert_rami_data_to_bids(raw_bids)


def save_new_bid(new_bid_data: Bid):
    bids_collection.insert_one(new_bid_data.__dict__)


def update_bid(existing_bid: SavedBid, new_bid_data: Bid):
    bids_collection.update_one({"_id": existing_bid.id}, {"$set": new_bid_data.__dict__})


def upsert_bid_data():
    for new_bid_data in new_bids_data:
        existing_bid = next(
            (existing_bid for existing_bid in existing_bids if existing_bid.bid_id == new_bid_data.bid_id),
            None)
        if existing_bid:
            if not new_bid_data.equals(existing_bid):
                update_bid(existing_bid, new_bid_data)
                bids_update_result.updated_bids_ids.append(new_bid_data.bid_id)
        else:
            save_new_bid(new_bid_data)
            bids_update_result.new_bids_ids.append(new_bid_data.bid_id)


def delete_irrelevant_bids():
    updated_bids_data_ids = [bid.bid_id for bid in new_bids_data]
    filter_criteria = {'bid_id': {'$nin': updated_bids_data_ids}}
    irrelevant_bids_records = bids_collection.find(filter_criteria)
    irrelevant_bids_ids = [bid.get('bid_id') for bid in irrelevant_bids_records]
    bids_update_result.deleted_bids_ids.extend(irrelevant_bids_ids)
    bids_collection.delete_many(filter_criteria)


upsert_bid_data()
delete_irrelevant_bids()
SessionContainer.close_session()


# Query existing from DB (Mongo)?
#       Downloaded $ brew cask install gcollazo-mongodb
#       Created /via/data/db
#       mongod --dbpath=/via/data/db - to run mongo
#       mongosh "mongodb://localhost:27017"
#       Downloaded shell from https://www.mongodb.com/try/download/shell
#       Moved its been to the same pass of the gcollazo-mongodb that were added to the PATH
# Compare - V
# Run in docker -
# Run on server periodically (K8S)
# FastAPI - https://www.mongodb.com/languages/python/pymongo-tutorial
# Notify in SMS on new bids
# Test
# Subscribe / Unsubscribe

#       mongod --dbpath=/via/data/db - to run mongo
#       mongosh "mongodb://localhost:27017"
#           use bids_db - to switch DB
#           db - to verify the DB your are at
#           show collections - to see all collections under a DB
#           db.bids.find({}) - to see all documents under bids
#           db.bids.updateOne({"_id": ObjectId("64f379d4569c2b055d17d0b2")}, {$set: {
#              is_online_bid: false
#            }})
