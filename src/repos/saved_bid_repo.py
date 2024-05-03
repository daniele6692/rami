from typing import List

from src.models.bids import SavedBid, Bid
from src.repos.base_repo import BaseRepo


class SavedBidRepo(BaseRepo):
    def __init__(self):
        collection_name = "bids"
        super(SavedBidRepo, self).__init__(collection_name, SavedBid)

    def delete_bids(self, current_bids: List[Bid]) -> List[int]:
        updated_bids_data_ids = [bid.bid_id for bid in current_bids]
        filter_criteria = {'bid_id': {'$nin': updated_bids_data_ids}}
        irrelevant_bids_records = self.get_all(filter_criteria)
        irrelevant_bids_ids = [bid.bid_id for bid in irrelevant_bids_records]
        self.delete(filter_criteria)
        return irrelevant_bids_ids
