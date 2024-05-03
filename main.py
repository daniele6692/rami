import logging

import uvicorn

from src.db_utils.session_container import SessionContainer
from fastapi import FastAPI
from src.routes.routes import router

app = FastAPI()
app.include_router(router, tags=["bids"], prefix="/bids")


@app.on_event("startup")
def startup_db_client():
    logging.info("App started")
    SessionContainer.get_session()


@app.on_event("shutdown")
def shutdown_db_client():
    logging.info("Bye Bye!")
    SessionContainer.close_session()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

# Q'sx
# Auth for the Mongo DB?

# Next Steps ->
# Separate local and docker ports
# Run on server periodically (K8S)
# Notify in SMS on new bids
# Test