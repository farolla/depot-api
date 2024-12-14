from pydantic import BaseModel
from typing import Optional, List

# Driver schemas
class DriverBase(BaseModel):
    name: str
    license_number: str
    experience: int

class DriverCreate(DriverBase):
    pass

class Driver(DriverBase):
    id: int

    class Config:
        from_attributes = True

# Bus schemas
class BusBase(BaseModel):
    model: str
    capacity: int
    year: int

class BusCreate(BusBase):
    pass

class Bus(BusBase):
    id: int

    class Config:
        from_attributes = True

# Route schemas
class RouteBase(BaseModel):
    number: str
    start_point: str
    end_point: str
    distance: float
    driver_id: int
    bus_id: int

class RouteCreate(RouteBase):
    pass

class Route(RouteBase):
    id: int

    class Config:
        from_attributes = True