#!/usr/bin/python3
"""Defines the FileStorage class.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Represents an abstracted storage engine.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in obj with key <obj_class_name>.id
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes objects to the JSON file.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file path to objects if it exists.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return