from typing import List

from src.utils.const import city_code_field_name, Villeges, audience_code_field_name, bid_preference_code_field_name, \
    no_preference_codes, designated_for_the_public_codes
from src.models.bids import Bid


class BidHelper:
    @staticmethod
    def convert_rami_data_to_bids(rami_data) -> List[Bid]:
        result = []
        for bid_data in rami_data:
            city_name = Villeges.get(bid_data.get(city_code_field_name))
            audience_code = bid_data.get(audience_code_field_name)
            bid_preference_code = bid_data.get(bid_preference_code_field_name)
            is_bid_with_preference = bid_preference_code in no_preference_codes
            for_private_structure = audience_code in designated_for_the_public_codes
            bid_with_city_name = {**bid_data, "city": city_name, "for_private_structure": for_private_structure,
                                  "is_bid_with_preference": is_bid_with_preference}
            current_bid = Bid(**bid_with_city_name)
            result.append(current_bid)
        return result
