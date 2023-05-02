import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorito = relationship("Favoritos_Personajes")

class Favoritos_Personajes(Base):
    __tablename__ = 'favorito_personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('user.id'), primary_key=True)
    personaje = Column(Integer, ForeignKey('character.id', primary_key=True))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    origin =  Column(String(250), nullable=False)
    favorito = relationship("Favoritos_Personajes")




def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
