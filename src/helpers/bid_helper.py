from typing import List

from src.utils.const import (
    CITY_CODE_FIELD_NAME,
    Villeges,
    AUDIENCE_CODE_FIELD_NAME,
    BID_PREFERENCE_CODE_FIELD_NAME,
    NO_PREFERENCE_CODES,
    DESIGNATED_FOR_THE_PUBLIC_CODES,
)
from src.models.bids import Bid


class BidHelper:
    @staticmethod
    def convert_rami_data_to_bids(rami_data) -> List[Bid]:
        result = []
        for bid_data in rami_data:
            city_name = Villeges.get(bid_data.get(CITY_CODE_FIELD_NAME))
            audience_code = bid_data.get(AUDIENCE_CODE_FIELD_NAME)
            bid_preference_code = bid_data.get(BID_PREFERENCE_CODE_FIELD_NAME)
            is_bid_with_preference = bid_preference_code in NO_PREFERENCE_CODES
            for_private_structure = audience_code in DESIGNATED_FOR_THE_PUBLIC_CODES
            bid_with_city_name = {
                **bid_data,
                "city": city_name,
                "for_private_structure": for_private_structure,
                "is_bid_with_preference": is_bid_with_preference,
            }
            current_bid = Bid(**bid_with_city_name)
            result.append(current_bid)
        return result
