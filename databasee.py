from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#from sqlalchemy.exe.declarative import declarative_base

SQLALCHEMY_DB_URL = "python+mysql://root:snehal@19@localhost/snehal"

engine=create_engine(SQLALCHEMY_DB_URL,connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()
