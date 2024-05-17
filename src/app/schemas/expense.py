from pydantic import BaseModel
from datetime import datetime

class ExpenseSchema(BaseModel):
    id: int
    date: datetime
    fk_category: int
    description: str
    value: int

    class Config:
        orm_mode = True