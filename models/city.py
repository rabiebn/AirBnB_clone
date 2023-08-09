#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a cityby these attributes:
        state_id : state id
        name : name of the city
    """

    state_id = ""
    name = ""
