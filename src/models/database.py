
import os
from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column, sessionmaker, Session
import re

load_dotenv(dotenv_path='.env')

class Base(DeclarativeBase, MappedAsDataclass):
    pass

def makeUrlDB() -> str:

    # build url DB for connection.
    db_url = os.getenv('DB_URL')
    db_url = re.sub('<LOGIN>', os.getenv('DB_CONNECTION_LOGIN'), db_url)
    db_url = re.sub('<PASSWORD>', os.getenv('DB_CONNECTION_PASSWORD'), db_url)
    db_url = re.sub('<DB_NAME>', os.getenv('DB_NAME'), db_url)
    
    return db_url

# make engine.
engine = create_engine(makeUrlDB(), echo=True)
session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def makeSession():
    session = session_maker()
    try:
        yield session
    except:
        session.rollback()
        raise
    finally:
        session.close()
