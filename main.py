import logging

from db_utils.session_container import SessionContainer
from fastapi import FastAPI
from routes.routes import router

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
def startup_db_client():
    logging.info("App started")
    SessionContainer.get_session()


@app.on_event("shutdown")
def shutdown_db_client():
    logging.info("Bye Bye!")
    SessionContainer.close_session()


# Query existing from DB (Mongo)?
#       Downloaded $ brew cask install gcollazo-mongodb
#       Created /via/data/db
#       mongod --dbpath=/via/data/db - to run mongo
#       mongosh "mongodb://localhost:27017"
#       Downloaded shell from https://www.mongodb.com/try/download/shell
#       Moved its been to the same pass of the gcollazo-mongodb that were added to the PATH
# FastAPI - https://www.mongodb.com/languages/python/pymongo-tutorial
# Compare - V
# Run in docker -
# Run on server periodically (K8S)
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
