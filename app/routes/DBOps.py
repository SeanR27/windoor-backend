from fastapi import APIRouter

from app.models.TableClasses import Week, Player, Opponent
from app.models.ReturnTableClasses import makeRowList
from app.models.AddEntry import addWeek, addPlayer, addOpponent
from app.models.RemoveEntry import removeEntry

router_weeks = APIRouter(prefix="/weeks")
router_players = APIRouter(prefix="/players")
router_opponents = APIRouter(prefix="/opponents")

# Get DB Contents
# ---------------
@router_weeks.get("/get")
def getWeeks(): return makeRowList(Week)
@router_players.get("/get")
def getPlayers(): return makeRowList(Player)
@router_opponents.get("/get")
def getOpponents(): return makeRowList(Opponent)


# Add DB Entry
# ------------
@router_weeks.get("/set")
def setWeeks(opponent:str, date:str, homeAway:bool, delta:int=0):
    addWeek(opponent, date, homeAway, delta)

@router_players.get("/set")
def setPlayers(firstName:str, lastName:str, court:int):
    addPlayer(firstName, lastName, court)

@router_opponents.get("/set")
def setOpponents(club:str, team:str):
    addOpponent(club, team)


# Remove DB Entry
# ---------------
@router_weeks.get("/remove")
def remWeek(id:int): removeEntry(id, Week)
@router_players.get("/remove")
def remPlayer(id:int): removeEntry(id, Player)
@router_opponents.get("/remove")
def remOpponent(id:int): removeEntry(id, Opponent)