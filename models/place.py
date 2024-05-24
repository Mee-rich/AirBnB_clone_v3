#!/usr/bin/python3
"""Module that creates a Place subclass"""
import os
from sqlalchemy import Table
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import Column
from models import storage_type
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60), ForeignKey('places.id'),
            primary_key=True, nullable=False),
            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                primary_key=True, nullable=False)
            )


class Place(BaseModel, Base):
    '''A Place to rent'''
    __tablename__ = 'place'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place', cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary="place_amenity", viewonly=False, backref='place_amenity')
    else:
        city_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_gueat = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''Returns a list of review instances with place_id
                equals to the current Place.id
                FileStorage relationship between Place and Review
            '''
            from models import storage
            all_reviews = storage.all(Review)
            alist = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    alist.append(review)
            return alist

        @property
        def amenities(self):
            ''' returns the list of Amenity instances
                based on the attribute amenity_ids that
                contains all Amenity.id linked to the Place
            '''
            from models import storage
            amens_all = storage.all(Amenity)
            alist = []
            for amen in amens_all.values():
                if amen.id in self.amenity_ids:
                    alist.append(amen)
            return alist

        @amenities.setter
        def amenities(self, obj):
            '''
                method  for adding an Amenity.id to the
                attribute amenity_ids, accepts only Amenity objects
            '''
            if obj is not None:
                if isinstance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
