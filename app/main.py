from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import MatchWeeksDBOps
from .routes import PlayersDBOps
from .routes import OpponentsDBOps

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

app.include_router(MatchWeeksDBOps.router)
app.include_router(PlayersDBOps.router)
app.include_router(OpponentsDBOps.router)

"""
deleteAllTables()
createTables()
"""