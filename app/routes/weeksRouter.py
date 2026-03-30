from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
from typing import List

from ..models.DBSchmea import engine, Week, WeekSchema


router = APIRouter(prefix="/weeks")

Session = sessionmaker(bind=engine)
session = Session()

@router.get("/get", response_model=List[WeekSchema])
def getWeeks():
    weeks = session.query(Week).all()
    return

@router.get("/set", response_model=List[WeekSchema])
def setWeeks():
    weeks = session.query(Week).all()
    return