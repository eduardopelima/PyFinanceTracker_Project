from fastapi import FastAPI
from app.routers import category, ai_response, expense

app = FastAPI()
routers = [category, ai_response, expense]

for r in routers:
    app.include_router(r.router)