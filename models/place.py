#!/usr/bin/python3
"""This is the place class"""
import models
from os import environ
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        amenities = relationship("Amenity",
                                 secondary="place_amenity", viewonly=False,
                                 back_populates="place_amenities")
        reviews = relationship('Review', backref='place')
    else:
        @property
        def reviews(self):
            """ decorator for review """
            n_list = []
            for key, obj in models.storage.items():
                if "Review" in key and obj.place_id == self.id:
                    n_list.append(obj)
            return n_list

        @property
        def amenities(self):
            """ amenities decorator """
            n_list = []
            for key in self.amenity_ids:
                n_list.append(models.storage.all().get("Amenity." + key))
            return n_list

        @amenities.setter
        def amenities(self, obj):
            """ doc string pend """
            if (obj.__class__.__name__ == "Amenity"):
                self.amenity_ids.append(str(obj.id))
