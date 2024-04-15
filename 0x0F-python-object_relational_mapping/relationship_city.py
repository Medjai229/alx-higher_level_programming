#!/usr/bin/python3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """
    This class inherits from Base and link to MySQL table citites
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
