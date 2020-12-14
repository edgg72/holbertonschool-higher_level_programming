#!/usr/bin/python3
"""
lists all State objects from a database
"""
from sys import argv
from model_state import Base, State
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    e = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                  argv[2],
                                                                  argv[3]))
    Base.metadata.create_all(e)
    Session = sessionmaker(bind=e)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print(str(state.id))
    else:
        print("Not found")
    session.close()
