import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(120))
    password = Column(String(100), nullable=False)

    def serialize(self):
        return{
            "id": self.id,
            "usermane": self.name,
        }

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo_url = Column(String(256), nullable=False)
    post_header = Column(String(256))
    date = Column(Integer, nullable=False, default=datetime.utcnow)

class Followers(Base):
    __tablename__ = 'followers' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('user.id'))

    
class Likes(Base):
    __tablename__ = 'Likes' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

class Coments(Base):
    __tablename__ = 'coments' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    coment = Column(String(256))



render_er(Base, 'diagram.png')