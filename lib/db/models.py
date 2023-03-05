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
            +f"\nKyle first name: {self.first_name} (duh dog)" \
            +f"\nKyle last name: {self.last_name}" \
            +f"\nKyle height: {self.height} Kyle feet" \
            +f"\nKyle heft: {self.weight} Kyle lbs" \
            +f"\nKyle superpower: {self.superpower}"

    kyle_cart = relationship("KyleCart", backref("kyle_item"))
    


class KyleCart(Base):
    __tablename__ = "kyle_carts"

    id = Column(Integer(), primary_key=True)

    kyle_id = Column(Integer(), ForeignKey("kyle_items.id"))

    def __repr__(self):
        return f"Kyle Cart: {self.id}"
