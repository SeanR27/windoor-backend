from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes.DBOps import router_weeks, router_players, router_opponents

from app.models.ReturnTableClasses import makeRowList
from app.models.Database import createTables, deleteAllTables


app = FastAPI(title="Windoor")

origins = [
    "http://localhost:5173", # Development
    "https://prc-management.vercel.app/" # Deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_weeks)
app.include_router(router_players)
app.include_router(router_opponents)

"""
deleteAllTables()
createTables()
"""