#!/usr/bin/python3
"""
__init__ Module defines:
    storage (FileStorage)
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
