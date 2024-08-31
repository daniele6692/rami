from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, AliasChoices


class Bid(BaseModel):
    bid_id: int = Field(validation_alias=AliasChoices("MichrazID", "bid_id"))
    city: str
    bid_status: int = Field(
        validation_alias=AliasChoices("StatusMichraz", "bid_status")
    )
    bid_book_published: bool = Field(
        validation_alias=AliasChoices("PublishedChoveret", "bid_book_published")
    )
    is_online_bid: bool = Field(
        validation_alias=AliasChoices("Mekuvan", "is_online_bid")
    )
    number_of_units: int = Field(
        validation_alias=AliasChoices("YechidotDiur", "number_of_units")
    )
    publish_date: Optional[str] = Field(
        validation_alias=AliasChoices("PirsumDate", "publish_date")
    )
    opening_date: Optional[str] = Field(
        validation_alias=AliasChoices("PtichaDate", "opening_date")
    )
    closing_date: Optional[str] = Field(
        validation_alias=AliasChoices("SgiraDate", "closing_date")
    )
    committee_date: Optional[str] = Field(
        validation_alias=AliasChoices("VaadaDate", "committee_date")
    )
    designated_public: Optional[int] = Field(
        validation_alias=AliasChoices("KhalYaadRashi", "designated_public")
    )
    bid_book_last_update_date: Optional[str] = Field(
        validation_alias=AliasChoices("ChoveretUpdateDate", "bid_book_last_update_date")
    )

    def equals(self, other_bid):
        if not isinstance(other_bid, Bid) and isinstance(other_bid) != dict:
            return False
        if isinstance(other_bid, Bid):
            other_bid = other_bid.__dict__
        # other_bid.pop("id", None)
        current_bid_dict = self.__dict__
        # current_bid_dict.pop("id", None)
        return all(
            other_bid[key] == current_bid_dict[key]
            for key in other_bid.keys()
            if key != "id"
        )


class SavedBid(Bid):
    id: ObjectId = Field(alias="_id")

    class Config:
        arbitrary_types_allowed = True
