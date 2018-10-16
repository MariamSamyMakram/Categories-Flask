import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Categories(Base):
    __tablename__='categories'

    category_id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

class Items(Base):
    __tablename__='items'

    id=Column(Integer,primary_key=True)
    title=Column(String(255),nullable=False)
    description=Column(String(255))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship(Categories)

class Users(Base):
    __tablename__='users'

    user_id=Column(Integer,primary_key=True)
    name=Column(String(255),nullable=False)

engine = create_engine('sqlite:///resturant.db')
Base.metadata.create_all(engine)

