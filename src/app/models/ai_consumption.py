from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from ..database import Base

class AiConsumption(Base):
    __tablename__ = "ai_consumption"

    id = Column(String, primary_key=True, index=True)
    created = Column(Integer, nullable=False)
    model = Column(String, nullable = False)
    usage_completion_tokens = Column(Integer, nullable=False)
    prompt_tokens = Column(Integer, nullable=False)
    total_tokens = Column(Integer, nullable=False)