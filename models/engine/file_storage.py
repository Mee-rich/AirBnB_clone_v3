#!/usr/bin/env python3
'''File Storage file'''

import json
import os
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User

class FileStorage():
    """File storage module"""
    
    """Class for storing and retrieving data
    Class Methods:
        all: Returns the object (dictionary object)
        new: updates the object id
        save: Converts Python objects into JSON strings
        reload: Converts JSON strings inton Python objects

    Class Attributs:
        __file_path (str): The name of the file, objects are saved to
        __objects (dict): A dictionary of instantiated objects
        class_dict (dict): A dictionary of all the classes
    """

    __file_path = "file.json"
    __objects = {}


    def all(self, cls=None):
        """returns all objects or ojects of a specified class"""
        if cls is None:
            return self.__objects
        else:
            filtered_dict = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    filtered_dict[key] = value
            return filtered_dict
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        self.__objects.update( 
                {obj.to_dict()['__class__'] + '.' + obj.id: obj}
        )

    def save(self):
        """saves a new obj"""
        objects = FileStorage.__objects
        file = FileStorage.__file_path
        content = {}

        for key, value in objects.items():
            content[key] = value.to_dict()

        with open(file, 'w', encoding="utf-8") as f:
            f.write(json.dumps(content))

    def reload(self):
        """reloads from a json file"""
        def is_valid_class(class_name):
            """Check if the class name is valid."""
            # Check if the class name exists in the global namespace
            return class_name in globals() and isinstance(globals()[class_name], type)

        file = FileStorage.__file_path

        try:
            if os.path.isfile(file):
                with open(file, 'r', encoding="utf-8") as f:
                    content = json.load(f)

                    for value in content.values():
                        class_name = value.get("__class__")
                        if class_name and is_valid_class(class_name):

                            obj_attrs = {k: v for k, v in value.items() if k != "__class__"}

                            # Create new instance of the class with extracted attributes
                            obj_instance = globals()[class_name](**obj_attrs)

                            # Add the new instance to your storage mechanism
                            self.new(obj_instance)
                        else:
                            # Log or handle invalid class names
                            pass
                    # print("Data reloaded successful.")
            else:
                print("JSON file not found.")
        except FileNotFoundError as e:
            print(f"Error loading data from file: {e}")

    def update(self, key, attr, value):
        """updates an instance"""
        if key in FileStorage.__objects:
            instance = FileStorage.__objects[key]
            setattr(instance, attr, value)
            instance.save()
        else:
            print("** no instance found **")
            
    def delete(self, obj=None):
        """Deletes an object from __objects"""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del FileStorage.__objects[key]

    def close(self):
        """Calls the reload method for deserializing the JSON file to objects"""
        self.reload()

