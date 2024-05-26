#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.amenity import Amenity

print("All objects: {}".format(storage.count()))
print("Amenity objects: {}".format(storage.count(Amenity)))

first_Amenity_id = list(storage.all(Amenity).values())[0].id
print("First Amenity: {}".format(storage.get(Amenity, first_Amenity_id)))
