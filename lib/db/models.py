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
    height = Column(Float())
    weight = Column(Float())
    superpower = Column(String())

    def __repr__(self):
        return f"Kyle id: {self.id}" \
            +f"Kyle first name: {self.first_name} duh dog" \
            +f"kyle last name: {self.last_name}" \
            +f"kyle height: {self.height}" \
            +f"kyle heft: {self.weight}" \
            +f"kyle superpower: {self.superpower}"

    