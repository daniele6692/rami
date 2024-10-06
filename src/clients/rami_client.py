import requests

from src.utils.const import OPEN_BIDS_IN_CENTER_AND_TEL_AVIV




class RamiClient:

    @staticmethod
    def get_raw_bids():
        response = requests.post("https://apps.land.gov.il/MichrazimSite/api/SearchApi/Search", json=OPEN_BIDS_IN_CENTER_AND_TEL_AVIV)
        return response.json()


