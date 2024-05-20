from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.expense import Expense
from ..schemas.expense import ExpenseSchema

router = APIRouter()

@router.post("/add/expense", response_model=ExpenseSchema)
def add_generativeai_expense(expense: ExpenseSchema, db: Session = Depends(get_db)):
    db_category = Expense(**expense.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category