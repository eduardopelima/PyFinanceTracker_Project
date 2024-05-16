from pydantic import BaseModel
from datetime import datetime

class CategorySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class ExpenseSchema(BaseModel):
    id: int
    date: datetime
    fk_category: int
    description: str
    value: int

    class Config:
        orm_mode = True
