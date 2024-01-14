#!/usr/bin/node
"""
file contains the class definition of a City
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    City Class
    ===========
    inherits from Base
    links to the MySQL table cities
    class attribute id:
        represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key
    class attribute name:
        represents a column of a string
        with maximum 128 characters and can’t be null
    class atttribute state_id:
        represents a column of an integer,
        can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
