from pydantic import BaseModel
from typing import Optional

class MessageSchema(BaseModel):
    content: str

class ChoiceSchema(BaseModel):
    message: MessageSchema

class UsageSchema(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int

class ChatCompletionSchema(BaseModel):
    id: str
    created: int
    model: str
    usage: UsageSchema
    choices: list[ChoiceSchema]