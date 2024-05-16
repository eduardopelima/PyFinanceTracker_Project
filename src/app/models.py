from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False)
    pub_date = Column(DateTime, default=func.now())

#class Expense(Base):
    #__tablename__ = "expenses"

    #id = Column(Integer, primary_key=True)
    #date = Column(DateTime)
    #fk_category = 
    #description: str
    #value: int

