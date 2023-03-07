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

    logs = relationship('KyleLog', backref="kyle_item")
    kyle_cart = relationship("KyleCart", backref("kyle_item"))

    def __repr__(self):
        return f"Kyle id: {self.id}" \
            +f"\nKyle first name: {self.first_name} (duh dog)" \
            +f"\nKyle last name: {self.last_name}" \
            +f"\nKyle height: {self.height} Kyle feet" \
            +f"\nKyle heft: {self.weight} Kyle lbs" \
            +f"\nKyle superpower: {self.superpower}"
    
class KyleLog(Base):
    __tablename__ = "kyle_logs"

    id = Column(Integer(), primary_key=True)
    kyle_id = Column(Integer(), ForeignKey('kyle_items.id'))
    last_name = Column(String())
    date_of_entry = Column(String())
    date_of_adoption = Column(String())

    def __repr__(self):
        return f"Log id: {self.id}" \
            +f"\nKyle id: {self.kyle_id}" \
            +f"\nKyle last name: {self.last_name}" \
            +f"\nDate of Entry: {self.date_of_entry}" \
            +f"\nDate of Adoption: {self.date_of_adoption}" \
            



    


class KyleCart(Base):
    __tablename__ = "kyle_carts"

    id = Column(Integer(), primary_key=True)

    kyle_id = Column(Integer(), ForeignKey("kyle_items.id"))

    def __repr__(self):
        return f"Kyle Cart: {self.id}"
