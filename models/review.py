#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review by these attributes:
        place_id : id of the place
        user_id : id of the user
        text : text review by the user
    """

    place_id = ""
    user_id = ""
    text = ""
