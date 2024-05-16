from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from .models import Category
from .schemas import CategorySchema
from .db import get_db

routers = APIRouter()

@routers.get("/")
def homeResponse():
    return {"Hello": "World"}

@routers.get("/sendQuestionToAI")
def sendQuestionToAI():
    return None

@routers.get("/listCategories", response_model=List[CategorySchema])
def listCategories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@routers.post("/addCategory", response_model=CategorySchema)
def addCategory(category: CategorySchema, db: Session = Depends(get_db)):
    
    print(category)
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category