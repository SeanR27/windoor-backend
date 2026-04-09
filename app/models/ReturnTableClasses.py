from app.models import TableClasses
from app.models.Database import Session

def makeRowList(TableClass):
    TableClass_to_ReturnClass = None

    if (TableClass == TableClasses.Week): TableClass_to_ReturnClass = Week_to_Return
    elif (TableClass == TableClasses.Player): TableClass_to_ReturnClass = None
    elif (TableClass == TableClasses.Opponent): TableClass_to_ReturnClass = Opp_to_Return


    session = Session()
    rows = session.query(TableClass).all()
    session.close()

    rowList = []
    for row in rows: rowList.append(TableClass_to_ReturnClass(row))
    for retRow in rowList: print(retRow)
    return rowList
    

def Week_to_Return(WeekObject:TableClasses.Week):
    class Week_ReturnClass():
        def __init__(self, WeekObject:TableClasses.Week):
            self.id:int = WeekObject.id

            session = Session()
            self.opp:str = session.query(TableClasses.Opp).filter(TableClasses.Opp.id == WeekObject.id).first()
            session.close()
            
            self.date_of_month:int = WeekObject.date_of_month
            self.month:int = WeekObject.month
            self.year:int = WeekObject.year
            self.home_away:bool = WeekObject.home_away
            self.points:int = WeekObject.points
            self.delta:int = WeekObject.delta

        def __str__(self):
            return f"Week Return Object || ID: {self.id}, Opponent: {self.opp}"
    
    return Week_ReturnClass(WeekObject)

def Opp_to_Return(OppObject:TableClasses.Opponent): return OppObject
