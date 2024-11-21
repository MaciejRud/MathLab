'''
Main file of cohort_manager.
'''


from fastapi import FastAPI

from src.utils.database import lifespan

app = FastAPI(lifespan=lifespan)

@app.post("/items/")
async def create_item(name: str, description: str):
    return {"name": name, "description": description}
