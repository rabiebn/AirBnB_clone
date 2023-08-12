#!/usr/bin/python3
"""
file_storage Module has:
    FileStorage Class.
"""
import models
import json


class FileStorage():
    """
    FileStorage class,  serializes instances to a JSON file
    and deserializes JSON file to instances.

    Private class attributes:
        __file_path (str) : path to the JSON file;
        __objects (dict)  : store all objects by <class name>.id.

    Public instance methods:
        __init__(self, *args, **kwargs)
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """
    __file_path = 'file.json'  # Might change this Later
    __objects = dict()

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj.to_dict()  # to_dict() ??

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass
