from typing import List

from src.helpers.bid_helper import BidHelper
from src.models.bid_update_result import BidsUpdateResult
from src.models.bids import Bid
from src.clients.rami_client import RamiClient
from src.repos.saved_bid_repo import SavedBidRepo


class BidsManager:

    def __init__(self):
        self.saved_bids_repo = SavedBidRepo()

    def get_bids(self) -> List[Bid]:
        all_bids = self.saved_bids_repo.get_all()
        return all_bids

    def sync_bids(self) -> BidsUpdateResult:
        bids_update_result = BidsUpdateResult()

        new_bids_data = self._get_new_bids_data()
        self._upsert_bid_data(new_bids_data, bids_update_result)
        self._delete_bids(new_bids_data, bids_update_result)

        return bids_update_result

    def _get_new_bids_data(self) -> List[Bid]:
        raw_bids = RamiClient.get_raw_bids()
        new_bids_data: List[Bid] = BidHelper.convert_rami_data_to_bids(raw_bids)
        return new_bids_data

    def _delete_bids(self, new_bids_data, bids_update_result: BidsUpdateResult):
        deleted_bids_ids = self.saved_bids_repo.delete_bids(new_bids_data)
        bids_update_result.deleted_bids_ids.extend(deleted_bids_ids)

    def _upsert_bid_data(
        self, new_bids_data: List[Bid], bids_update_result: BidsUpdateResult
    ):
        existing_bids = self.saved_bids_repo.get_all()
        for new_bid_data in new_bids_data:
            existing_bid = next(
                (
                    existing_bid
                    for existing_bid in existing_bids
                    if existing_bid.bid_id == new_bid_data.bid_id
                ),
                None,
            )
            if existing_bid:
                if not new_bid_data.equals(existing_bid):
                    self.saved_bids_repo.update(existing_bid, new_bid_data.__dict__)
                    bids_update_result.updated_bids_ids.append(new_bid_data.bid_id)
            else:
                self.saved_bids_repo.save(new_bid_data)
                bids_update_result.new_bids_ids.append(new_bid_data.bid_id)
