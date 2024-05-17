from fastapi import FastAPI
from .routers import category, ai_response, expense

app = FastAPI()
routers = [category, ai_response, expense]

for r in routers:
    app.include_router(r.router)