import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String, nullable=False, unique=True)
    subscription_date = Column(String)
    is_login = Column(Boolean, nullable=False)

class Profiles(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(30), nullable=False, unique=True)
    image_url = Column(String)
    description = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship(Users)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    content = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_followers = Column(Integer, ForeignKey('users.id'))
    user_following = Column(Integer, ForeignKey('users.id'))
    followers = relationship(Users)
    following = relationship(Users)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment = Column(String(300))
    post_id = Column(Integer, ForeignKey('posts.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    post = relationship(Posts)
    user = relationship(Users)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
