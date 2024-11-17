'''
Main file of projects.
'''


from fastapi import FastAPI

from MathLab.core.database import lifespan

app = FastAPI(lifespan=lifespan)

