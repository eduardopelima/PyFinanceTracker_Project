from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

Base = declarative_base()

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False)
    pub_date = Column(DateTime, default=func.now())
