#!/usr/bin/python3
"""This Defines the State class."""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """Represents a state for a MySQL database.
        
        Inherits from SQLAlchemy Base and links to the MySQL table states.

        Attributes:
            __tablenames__ (str): The name of the MySQL table to store States
            name (sqlalchemy String): The name of the State.
            cities (sqlalchemy relationship): The State-City relationship.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the cities in this state"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
