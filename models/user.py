#!/usr/bin/python3
'''This Module creates a User class'''
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    '''user class object'''
    # Note storage type = getenv option
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                cascade='all, delete, delete-orphan')
        reviews = relationship('Review', backref='user',
                cascade='all, delete, delete-orphan')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
