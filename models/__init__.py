#!/usr/bin/python3
"""
Initialization script for the models directory.
"""

from engine.file_storage import FileStorage

# Create an instance of FileStorage
storage = FileStorage()

# Reload data from storage
storage.reload()
