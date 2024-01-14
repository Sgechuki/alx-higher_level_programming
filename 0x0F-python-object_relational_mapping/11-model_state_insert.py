#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database hbtn_0e_6_usa
script should take 3 arguments: username, password and database name
Print the new states.id after creation
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
    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    latest = session.query(State).filter(State.name == "Louisiana").first()
        print("{}".format(latest.id))
    session.close()
