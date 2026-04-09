from fastapi import APIRouter, HTTPException

from app.models.TableClasses import Week
from app.models.ReturnTableClasses import makeRowList
from app.models.Database import Session, viewTableData

import datetime

router = APIRouter(prefix="/weeks")

@router.get("/get")
def getWeeks():
    rowList = makeRowList(Week)
    return rowList

@router.get("/set")
def setWeeks(opponent:str, date:str, homeAway:bool=None, delta:int=0):
    # Turn Opp String

    # Split Date String Into Integers: DD, MM, YYYY
    dateArr = date.split("/")
    try:
        date = int(dateArr[0])
        month = int(dateArr[1])
        year = int(dateArr[2])
        datetime.date(year, month, date)
    except:
        raise HTTPException(status_code=422, detail="Invalid Date")

    weekRow = Week( opp_id = 0,
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
    viewTableData(Week)