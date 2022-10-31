from sqlalchemy import (
    create_engine, Column, String, ForeignKey, Integer)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os


BASE_DIR=os.path.dirname(os.path.realpath(__file__))

conn="sqlite:///"+os.path.join(BASE_DIR,"SLS_database")
#connect to database 
engine = create_engine(conn, echo=True)

#manage tables
Base = declarative_base()                        



#users tabel
class Users ( Base ):
    __tablename__ = "users"

    student_nr = Column(String(), primary_key=True)
    name = Column(String())

    loans = relationship("Loans", backref="author", lazy=True)

    def __init__ (self, student_nr, name):
        self.student_nr = student_nr
        self.name = name


# loans table
class Loans ( Base ):
    __tablename__ = "loans"
    item_id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    student_nr = Column(String(), ForeignKey(Users.student_nr))
    date = Column(String())

    def __init__ (self, student_nr, item_id, item_name, date):
        self.student_nr = student_nr
        self.item_id = item_id
        self.item_name = item_name
        self.date = date


Base.metadata.create_all(engine)
session=sessionmaker()(bind=engine)
    
