import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Favoritos_Personajes(Base):
    __tablename__ = 'favoritos_personaje'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(ForeignKey('users.id'), primary_key=True)
    character_id = Column(ForeignKey('characters.id'), primary_key=True)
    character = relationship('Character', back_populates='users')
    user = relationship('User', back_populates='characters')

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    characters = relationship('Favoritos_Personajes', back_populates='user')


class Character(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    status = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    origin =  Column(String(250), nullable=False)
    favorito = relationship('Favoritos_Personajes')
    users = relationship('Favoritos_Personajes', back_populates='character')


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
