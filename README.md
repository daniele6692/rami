# RAMI Bids Updator


## How to run the project locally 
1. [Make sure your Mongo is running locally](#installing--running-mongo-locally-on-mac)
2. set the env var to be MONGO_URL = mongodb://127.0.0.1:27017


### How to install Mongo locally on MAC:
1. `brew cask install gcollazo-mongodb`
2. `mkdir /via/data/db`


### How to run Mongo locally on MAC:
1. `mongod --dbpath=/via/data/db` - to run mongo
   1. `mongod --fork --syslog --dbpath=/via/data/db` - to run in the background


### Installing Mongo Shell locally:
1. Downloaded shell from https://www.mongodb.com/try/download/shell
2. Moved its bin to the same pass of the gcollazo-mongodb that were added to the PATH
   1. in my case it was under `/Applications/MongoDB.app/Contents/Resources/Vendor/mongodb/bin`
3. `mongosh "mongodb://localhost:27017"` - to start shell vs local Mongo


## How to run in Docker & useful commands 
1. RAMI_STAGE=dev docker compose up --build web-server -d
2. RAMI_STAGE=dev docker-compose up --build --force-recreate --renew-anon-volumes -d
3. docker compose down
4. docker logs -f web-server
5. docker build -t <some tag> .
6. docker exec -it mongo-db mongosh <"mongodb://<user>:<pass>@localhost:27017/admin">


### Useful Mongo Commands:
1. `use bids_db` - To switch DB's (schemes) 
2. `db` - To verify the DB you are currently at
3. `show collections` - to see all collections under current DB
4. `db.bids.find({})` - to see all documents under bids collection
5. `db.bids.updateOne({"_id": ObjectId("64f379d4569c2b055d17d0b2")}, {$set: {is_online_bid: false}})` - an example for an update command

