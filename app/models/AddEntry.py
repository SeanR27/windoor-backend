from fastapi import HTTPException;

from app.models.TableClasses import Week, Player, Opponent
from app.models.ReturnTableClasses import makeRowList
from app.models.Database import Session

import datetime

def addWeek(opponent:str, date:str, homeAway:bool=None, delta:int=0):
    # Turn Opp String
    session = Session()
    oppID = session.query(Opponent).filter((Opponent.team == opponent)).first().id
    session.close()

    # Split Date String Into Integers: DD, MM, YYYY
    dateArr = date.split("/")
    try:
        date = int(dateArr[0])
        month = int(dateArr[1])
        year = int(dateArr[2])
        datetime.date(year, month, date)
    except:
        raise HTTPException(status_code=422, detail="Invalid Date")

    weekRow = Week( opp_id = oppID,
                    date_of_month = dateArr[0],
                    month = dateArr[1],
                    year = dateArr[2],
                    home_away = homeAway,
                    delta = delta
                    )
    
    session = Session()
    session.add(weekRow)
    session.commit()
    session.close()

def addPlayer(): None

def addOpponent(club, team):
    session = Session()
    teamExists = session.query(Opponent).filter((Opponent.club == club) & (Opponent.team == team)).first()
    session.close()

    # Raises HTTP Error if the specified team already exists
    if (teamExists != None): raise HTTPException(status_code=422, detail="Team Already Exists")

    session = Session()
    session.add(Opponent(club = club, team = team))
    session.commit()
    session.close()