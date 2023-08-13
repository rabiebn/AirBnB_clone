#!/usr/bin/python3
"""
file_storage Module defines:
    FileStorage Class.
"""
from models.base_model import BaseModel
from models.user import User
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
    __file_path = 'file.json'
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
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        objs_dict = dict()
        for k, obj in self.__objects.items():
            objs_dict[k] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objs_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                        cls_name = o["__class__"]
                        del o["__class__"]
                        self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            pass
