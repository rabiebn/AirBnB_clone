#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User by these attributes :
        email : The email of the user.
        password : The password of the user.
        first_name : The first name of the user.
        last_name : The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
