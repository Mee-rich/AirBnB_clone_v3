#!/usr/bin/python3
"""This module creates a Review subclass"""
import os
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """Represents a review for a MySQL database.
        Inherits from SQLAlchemy Base and links to MySQL table reviews.
        
        Attributes:
            __tablename__ (str): The name of the MySQL table to store Reviews.
            test (sqlalchemy String): The review description.
            place_id (sqlalchemy String): The review's place id.
            user_id (sqlalchemy String): The review's user id.
    """
    __tablename__ = 'reviews'   
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
