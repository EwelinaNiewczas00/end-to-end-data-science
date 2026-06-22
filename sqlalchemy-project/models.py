
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Table, ForeignKey
from datetime import datetime

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    category = Column(String(100))
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

# --- ZADANIE 9: FILMY I AKTORZY ---

movie_actor_association = Table(
    'movie_actor', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('actor_id', Integer, ForeignKey('actors.id'), primary_key=True)
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    actors = relationship("Actor", secondary=movie_actor_association, back_populates="movies")

class Actor(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    movies = relationship("Movie", secondary=movie_actor_association, back_populates="actors")

# --- ZADANIE 12: ARTYKUŁY ---
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text)
