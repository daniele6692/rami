import requests

from const import open_bids_in_center_and_tel_aviv


class RamiClient:

    @staticmethod
    def call_rami():
        response = requests.post('https://apps.land.gov.il/MichrazimSite/api/SearchApi/Search',
                                 json=open_bids_in_center_and_tel_aviv)
        return response.json()
