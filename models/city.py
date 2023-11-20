#!/usr/bin/python3
"""Defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city
    Attributes:
        state_id (str): ID State.
        name (str): City Name.
    """

    state_id = ""
    name = ""
