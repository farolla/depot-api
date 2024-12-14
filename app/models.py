from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base

class Driver(Base):
    __tablename__ = "drivers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    license_number = Column(String, unique=True)
    experience = Column(Integer)
    
    routes = relationship("Route", back_populates="driver")

class Bus(Base):
    __tablename__ = "buses"
    
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    capacity = Column(Integer)
    year = Column(Integer)
    
    routes = relationship("Route", back_populates="bus")

class Route(Base):
    __tablename__ = "routes"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String)
    start_point = Column(String)
    end_point = Column(String)
    distance = Column(Float)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    bus_id = Column(Integer, ForeignKey("buses.id"))
    
    driver = relationship("Driver", back_populates="routes")
    bus = relationship("Bus", back_populates="routes")