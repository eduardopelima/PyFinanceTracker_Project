from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from ..database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable = False)
    pub_date = Column(DateTime, default=func.now())

    expenses = relationship("Expense", back_populates="category")
