import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favoritos_personajes= Table(
    "favoritos_personajes",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("character_id", ForeignKey("character.id")),
)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    lastname = Column(String(250))
    username = Column(String(250))
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorito = relationship("Favoritos_Personajes")

# class Favoritos_Personajes(Base):
#     __tablename__ = 'favorito_personaje'
#     user_id = Column(Integer, ForeignKey('user.id'))
#     personaje = Column(Integer, ForeignKey('character.id'))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    status = Column(String(250))
    gender = Column(String(250))
    species = Column(String(250))
    origin =  Column(String(250))
    favorito = relationship("Favoritos_Personajes")




def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
