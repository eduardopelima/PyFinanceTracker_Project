from fastapi import APIRouter, Depends
from typing import List
import json
from datetime import datetime
from sqlalchemy.orm import Session

from .models import Category
from .schemas import CategorySchema, ExpenseSchema
from .db import get_db
from .ai import PromptExpense

routers = APIRouter()



@routers.get("/")
def homeResponse():
    return {"Hello": "World"}

@routers.get("/list/categories", response_model=List[CategorySchema])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@routers.post("/add/category", response_model=CategorySchema)
def add_category(category: CategorySchema, db: Session = Depends(get_db)):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@routers.get("/get/generativeai/expense")
def get_generativeai_expense(user_expense_description: str, db: Session = Depends(get_db)):
    
    categoriesList = list_categories(db)
    current_datetime = datetime.now()
    output_schema = ExpenseSchema.model_json_schema()
    user_expense_description = "comprei uma paçoca por 2 reais no restaurante"

    categoriesDict = []
    for category in categoriesList:
        categoryId = category.id
        categoryName = category.name

        categoryJson = {
            "id": categoryId,
            "name": categoryName
        }

        categoriesDict.append(categoryJson)

    promptExpense = PromptExpense(description=user_expense_description, current_datetime=current_datetime, expenses_categories=categoriesDict, output_schema=output_schema) 
    promptToAi = promptExpense.get_ai_response()

    print(promptToAi)
    return promptToAi

@routers.get("/add/expense")
def add_generativeai_expense():
    return None