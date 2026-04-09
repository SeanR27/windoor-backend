from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.schema import DropTable
from sqlalchemy.ext.compiler import compiles

import os
from dotenv import load_dotenv

from app.models.TableClasses import Base

load_dotenv()

engine = create_engine(os.getenv("CONNECTION_STRING"))
Session = sessionmaker(bind=engine)

def createTables():
    Base.metadata.create_all(engine)
    print("All tables created")

def deleteAllTables():
    @compiles(DropTable, "postgresql")
    def _compile_drop_table(element, compiler, **kwargs):
        return compiler.visit_drop_table(element) + " CASCADE"
    
    Base.metadata.drop_all(bind=engine)
    print("All tables deleted.")

def viewTableData(TableClass):
    session = Session()
    data = session.query(TableClass).all()
    session.close()
    for row in data: print(row)
