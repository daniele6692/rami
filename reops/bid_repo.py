from models.bids import SavedBid
from reops.base_repo import BaseRepo


class BidRepo(BaseRepo):
    def __init__(self):
        collection_name = "bids"
        super(BidRepo, self).__init__(collection_name, SavedBid)
