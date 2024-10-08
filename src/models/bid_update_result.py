from typing import Optional, List

from pydantic import BaseModel, Field


class BidsUpdateResult(BaseModel):
    new_bids_ids: List[int] = Field(default=[])
    updated_bids_ids: List[int] = Field(default=[])
    deleted_bids_ids: List[int] = Field(default=[])
