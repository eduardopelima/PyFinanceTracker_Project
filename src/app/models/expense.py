from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, Numeric, String
from ..database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    recurrency = Column(Boolean, default=False)
    fk_category = Column(Integer, ForeignKey('categories.id'), nullable=False)
    description = Column(String)
    value = Column(Numeric(10,2))

    category = relationship("Category", back_populates="expenses")