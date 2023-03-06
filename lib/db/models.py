from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class KyleItem(Base):
    __tablename__ = "kyle_items"

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    