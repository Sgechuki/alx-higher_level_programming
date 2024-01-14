#!/usr/bin/python3
"""
cript that deletes all State objects with a name containing the letter a
script should take 3 arguments: username, password and database name
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).where(State.name.like("%a%"))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
