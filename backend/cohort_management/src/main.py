'''
Main file of cohort_manager.
'''


from fastapi import FastAPI

from backend.cohort_management.src.utils.database import lifespan

app = FastAPI(lifespan=lifespan)

