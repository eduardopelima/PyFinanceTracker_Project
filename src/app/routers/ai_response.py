from fastapi import APIRouter, Depends
from typing import List
import json
from datetime import datetime
from sqlalchemy.orm import Session

from ..models.db_config import get_db
from ..schemas.ai_response import ChatCompletionSchema
from ..schemas.expense import ExpenseSchema
from .category import list_categories
from ..ai import PromptExpense

router = APIRouter()

@router.get("/get/generativeai/expense")
def get_generativeai_expense(user_expense_description: str, db: Session = Depends(get_db)):
    
    categoriesList = list_categories(db)
    current_datetime = datetime.now()
    output_schema = ExpenseSchema.model_json_schema()

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
    aiResponse = promptExpense.get_ai_response()

    #validated_data = ChatCompletionSchema(**aiResponse)

    return aiResponse #aiResponse['choices']['message']['content']

#@routers.post("/add/generativeai/ai_consumption", response_model=ChatCompletionSchema)
#def add_generativeai_ai_consuption(db: Session = Depends(get_db), aiResponse):

#    id = aiResponse['id']
#    created_at = aiResponse['created']
#    model = aiResponse['model']
#    usageCompletionTokens = aiResponse['usage']['completion_tokens']
#    promptTokens = aiResponse['usage']['prompt_tokens']
#    totalTokens = aiResponse['usage']['total_tokens']

#    return aiResponse