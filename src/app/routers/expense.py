from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas.expense import ExpenseSchema

router = APIRouter()

@router.get("/add/expense")
def add_generativeai_expense():
    return None