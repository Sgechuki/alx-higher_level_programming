#!/usr/bin/python3
"""
cript that deletes all State objects with a name containing the letter a
script should take 3 arguments: username, password and database name
Results must be sorted in ascending order by cities.id
"""

from sys import argv
from sqlalchemy import create_engine
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for c, s in session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.commit()
    session.close()
