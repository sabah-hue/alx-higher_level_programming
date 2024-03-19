#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sys import argv

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
new = State(name="Louisiana")
session.add(new)
session.commit()
print(new.id)
session.close()
