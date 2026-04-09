from fastapi import APIRouter, HTTPException

from app.models.TableClasses import Opponent
from app.models.ReturnTableClasses import makeRowList
from app.models.Database import Session, viewTableData

router = APIRouter(prefix="/opponents")

@router.get("/get")
def getOpps():
    rowList = makeRowList(Opponent)
    return rowList

@router.get("/set")
def setOpps(club:str, team:str):
    session = Session()
    existantTeam = session.query(Opponent).filter((Opponent.club == club) & (Opponent.team == team)).first()
    session.close()

    # Raises HTTP Error if the specified team already exists
    if (existantTeam != None): raise HTTPException(status_code=422, detail="Team Already Exists")

    session = Session()
    session.add(Opponent(club = club, team = team))
    session.commit()
    session.close()