#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place by these attributes :
        city_id : the id of the city
        user_id : the id of the user
        name : name of the place
        description : a description of the place
        number_rooms : number of the rooms
        number_bathrooms : number of the bathrooms
        max_guest : the max number of guests allowed
        price_by_night : price of the room
        latitude : latitude of the place
        longitude : longitude of the place
        amenity_ids : list of amenity ids
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
