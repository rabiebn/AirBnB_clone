#!/usr/bin/python3
"""
__init__ Module has:
    storage (FileStorage)
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
