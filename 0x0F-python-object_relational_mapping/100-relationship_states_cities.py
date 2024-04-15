#!/usr/bin/python3
"""
This script that creates the State “California” with
the City “San Francisco” from the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from relationship_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    sanF = City(name="San Francisco", state=State(name="California"))
    session.add(sanF)
    session.commit()
