#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, relationship, backref

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine, checkfirst=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for states in session.query(State).order_by(State.id).all():
        print("{}: {}".format(states.id, states.name))
        for cities in session.query(City).order_by(City.id).all():
            if states.id == cities.state_id:
                print("\t{}: {}".format(cities.id, cities.name))
    session.commit()
    session.close()
