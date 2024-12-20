'''
Main file of cohort_manager.
'''


from fastapi import FastAPI

from src.utils.database import lifespan
from src.auth.routers import router as auth_router
#from src.utils.swagger_config import get_swagger_config

app = FastAPI(lifespan=lifespan)

@app.post("/items/")
async def create_item(name: str, description: str):
    return {"name": name, "description": description}

app.include_router(auth_router, prefix="")

