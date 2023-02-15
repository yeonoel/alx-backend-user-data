#!/usr/bin/env python3
""" Create User Model with sqlalchemy """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ The model will have the following attributes: """
    __tablename__ = 'users'

    id = Column(Integer, primary_Key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
