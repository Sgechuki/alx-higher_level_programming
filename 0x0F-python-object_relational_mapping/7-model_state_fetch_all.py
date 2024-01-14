#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
script should take 3 arguments: username, password and database name
Results must be sorted in ascending order by states.id
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
    for obj in session.query(State).order_by(State.id):
        print("{}: {}".format(obj.id, obj.name))
    session.close()
