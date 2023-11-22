from fastapi import APIRouter, Request, status

from managers.bids_manager import BidsManager

router = APIRouter()


@router.get("/sync-bids", response_description="Sync Bids Details", status_code=status.HTTP_200_OK)
def create_book(request: Request):
    # manager = BidsManager()
    # manager.sync_bids()
    return {"message": "Welcome to the PyMongo tutorial!"}
