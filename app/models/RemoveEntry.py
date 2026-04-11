from app.models.Database import Session
from app.models.TableClasses import Week, Player, Opponent

def removeEntry(id, TableClass):

    TCArray = [Week, Player, Opponent]
    if (TableClass not in TCArray ): print("removeEntry() from RemoveEntry.py received an incompatible Table Class argument."); return None

    session = Session()
    targetEntry = session.query(TableClass).filter(TableClass.id == id).first()
    session.delete(targetEntry)
    session.commit()
    session.close()


