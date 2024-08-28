import requests

from src.utils.const import open_bids_in_center_and_tel_aviv


class RamiClient:

    @staticmethod
    def get_raw_bids():
        response = requests.post(
            "https://apps.land.gov.il/MichrazimSite/api/SearchApi/Search",
            json=open_bids_in_center_and_tel_aviv,
        )
        return response.json()
