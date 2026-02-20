from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

USER="root"
PASSWORD = "password"
HOST ="localhost"
PORT ="3306"
DB = "fastapi_crud"

DATABASE_URL = F"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"

# creating the connection

engine = create_engine(DATABASE_URL)

# create a session / for refering the database during api intraction

Session = sessionmaker(autoflush=False,autocommit=False,bind=engine)


def get_DB():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# Base

Base = declarative_base()
