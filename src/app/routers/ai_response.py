from fastapi import APIRouter, Depends
import json
from datetime import datetime
from sqlalchemy.orm import Session

from ..database import get_db
from ..chatgpt.schemas import ChatCompletionSchema
from ..schemas.expense import ExpenseSchema
from .category import list_categories
from ..chatgpt.prompt import PromptExpense
from ..models.ai_consumption import AiConsumption

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

    add_generativeai_ai_consumption(aiResponse, db)

    expensesList = json.loads(aiResponse.choices[0].message.content)

    return expensesList

@router.post("/add/generativeai/ai_consumption", response_model=ChatCompletionSchema)
def add_generativeai_ai_consumption(aiResponse: ChatCompletionSchema, db: Session = Depends(get_db)):

    id = aiResponse.id
    created = aiResponse.created
    model = aiResponse.model
    usageCompletionTokens = aiResponse.usage.completion_tokens
    promptTokens = aiResponse.usage.prompt_tokens
    totalTokens = aiResponse.usage.total_tokens

    test = {
        'id': id,
        'created': created,
        'model': model,
        'usage_completion_tokens': usageCompletionTokens,
        'prompt_tokens': promptTokens,
        'total_tokens': totalTokens
    }

    db_ai_consumption = AiConsumption(**test)
    db.add(db_ai_consumption)
    db.commit()
    db.refresh(db_ai_consumption)
    return db_ai_consumption
