import asyncio

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from src.db_utils.session_container import SessionContainer
from src.managers.bids_manager import BidsManager
from src.routes.routes import router
from src.utils.const import BIDS_SYNC_INTERVAL_IN_SECONDS
from src.utils.env_utils import get_env_file_path, is_running_locally

app = FastAPI()
app.include_router(router, tags=["bids"], prefix="/bids")


@app.on_event("startup")
def startup_db_client():
    print("App started", flush=True)
    _load_env_file()
    asyncio.create_task(_sync_bids())
    SessionContainer.init_session()


@app.on_event("shutdown")
def shutdown_db_client():
    print("Bye Bye!")


async def _sync_bids():
    while True:
        await asyncio.sleep(BIDS_SYNC_INTERVAL_IN_SECONDS)
        print("About to run periodical sync", flush=True)
        manager = BidsManager()
        manager.sync_bids()
        print("Periodical sync completed")


def _load_env_file():
    print("_load_env_file")
    if is_running_locally():
        env_path = get_env_file_path()
        is_successful = load_dotenv(env_path)
        print(f".env file loaded successfully: {is_successful}")


if __name__ == "__main__":
    print("Starting app")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


# Next Steps ->
# Git pre-commit-hooks
# 1. Make sure it checks only my current changes
# 2. add the checks to the pipeline and make sure it fails when needed

# Auto Align all repo according to python best practices
# Deploy to "live"
# K8S?
# CI + Tests
# Auth for the Mongo DB locally
# Notify in SMS on new bids
