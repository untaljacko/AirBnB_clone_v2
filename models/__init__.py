#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine import db_storage
    storage = db_storage.DBStorage()
    storage.reload()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()
    storage.reload()
