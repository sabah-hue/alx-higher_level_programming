#!/usr/bin/python3
"""
script that  prints all City objects from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City)
    .join(State, City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
