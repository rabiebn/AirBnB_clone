#!/usr/bin/python3
"""
user Module defines:
    User Class.
"""

from base_model import BaseModel


class User(BaseModel):
    """
    User Class.

    Public class attributes:
        email (string);
        password (string);
        first_name (string);
        last_name(string).
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
