import asyncio
import logging

import uvicorn

from src.db_utils.session_container import SessionContainer
from fastapi import FastAPI

from src.managers.bids_manager import BidsManager
from src.routes.routes import router
from src.utils.const import bids_sync_interval_in_seconds

app = FastAPI()
app.include_router(router, tags=["bids"], prefix="/bids")


@app.on_event("startup")
def startup_db_client():
    asyncio.create_task(_sync_bids())
    logging.info("App started")
    SessionContainer.get_session()


@app.on_event("shutdown")
def shutdown_db_client():
    logging.info("Bye Bye!")
    SessionContainer.close_session()


async def _sync_bids():
    while True:
        await asyncio.sleep(bids_sync_interval_in_seconds)
        manager = BidsManager()
        manager.sync_bids()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# Q'sx
# Auth for the Mongo DB?

# Next Steps ->
# CI
# K8S
# Notify in SMS on new bids
# Test