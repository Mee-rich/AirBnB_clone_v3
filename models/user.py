#!/usr/bin/python3
'''This Module creates a User class'''
from models import storage_type
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from hashlib import md5

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


    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = self.hash_password(kwargs['password'])

    @staticmethod
    def hash_password(password):
        """Hashes the password using MD5"""
        return md5(password.encode()).hexdigest()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self.hash_password(value)

    def save(self):
        """Save the object to storage"""
        self._password = self.password  # Ensure password is hashed
        super().save()
