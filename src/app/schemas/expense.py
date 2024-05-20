from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal

class ExpenseSchema(BaseModel):
    id: int
    date: datetime
    recurrency: bool
    fk_category: int
    description: str
    value: Decimal = Field(decimal_places=2)

    class Config:
        orm_mode = True