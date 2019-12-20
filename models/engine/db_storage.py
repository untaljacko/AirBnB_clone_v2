#!/usr/bin/python3
""" New engine storage for Airbnb project """
import json
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ new class for DBStorage engine """
    __engine = None
    __session = None
    __list_class = [State, User, City, Amenity, Review, Place]

    def __init__(self):
        """ method documentation """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD'],
            environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB']),
            pool_pre_ping=True)
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ method documentation """
        new_dic = {}
        if cls is not None:
            all_obj = self.__session.query(eval(cls))
            for obj in all_obj:
                key = ".".join([cls, obj.id])
                new_dic.update({key: obj})
        else:
            for cl in self.__list_class:
                all_obj = self.__session.query(cl)
                for obj in all_obj:
                    key = ".".join([cls, obj.id])
                    new_dic.update({key: obj})
        return new_dic

    def new(self, obj):
        """ method documentation for new """
        self.__session.add(obj)

    def save(self):
        """ method documentation for save """
        self.__session.commit()

    def delete(self, obj=None):
        """ method documentation for delete """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ method documentation for reload """
        Base.metadata.create_all(self.__engine)
        current_se = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(current_se)()

    def close(self):
        """ for close the sqlalchemy session """
        self.__session.close()
