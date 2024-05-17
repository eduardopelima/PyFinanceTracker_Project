from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    #fk_category = 
    description: str
    value: int