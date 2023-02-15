#!/usr/bin/env python3
"""
User Model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ User Model """
    __tablename__ = 'users'
    id = Column(Integer, primary_Key=True)
    name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String(225))
    reset_token = Column(String(225))
