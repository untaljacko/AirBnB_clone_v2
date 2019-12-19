#!/usr/bin/python3
"""This is the state class"""
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', backref="state")
    else:
        @property
        def cities(self):
            """ decorator for cities class
            """
            new_list = []
            for key, obj in models.storage.all().items():
                if 'City' in key and obj.state_id == self.id:
                    new_list.append(obj)
            return new_list
