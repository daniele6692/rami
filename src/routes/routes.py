from typing import List

from fastapi import APIRouter, Request, status

from src.managers.bids_manager import BidsManager
from src.models.bids import Bid

router = APIRouter()


@router.get("/sync", response_description="Sync Bids Details", status_code=status.HTTP_200_OK)
def sync_bids(request: Request):
    manager = BidsManager()
    manager.sync_bids()
    return {"message": "Bids are now synced"}


@router.get("/get", response_description="Sync Bids Details", status_code=status.HTTP_200_OK, response_model=List[Bid])
def get_bids(request: Request):
    manager = BidsManager()
    bids: List[Bid] = manager.get_bids()
    return bids