'''
Main file of cohort_manager.
'''


from fastapi import FastAPI

from src.utils.database import lifespan

app = FastAPI(lifespan=lifespan)

