from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from ..models.db_config import get_db
from ..models.category import Category
from ..schemas.category import CategorySchema

router = APIRouter()

@router.get("/list/categories", response_model=List[CategorySchema])
def list_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

@router.post("/add/category", response_model=CategorySchema)
def add_category(category: CategorySchema, db: Session = Depends(get_db)):
    db_category = Category(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category