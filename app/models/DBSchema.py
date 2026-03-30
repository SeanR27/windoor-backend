from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship

from pydantic import BaseModel

import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.getenv("CONNECTION_STRING"))
Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lasstName = Column(String)
    court = Column(Integer)
    games_total = Column(Integer)
    position_games = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)
    performance = Column(Integer)
    weightedScore = Column(Integer)

    matches = relationship("Match", back_populates="players")

class Week(Base):
    __tablename__ = "weeks"

    id = Column(Integer, primary_key=True)
    opp_id = Column(Integer, ForeignKey("opponents.id"))
    home_away = Column(Boolean)
    points = Column(Integer)
    delta = Column(Integer)

    opponents = relationship("Opp", back_populates="weeks")

class Opp(Base):
    __tablename__ = "opponents"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    weeks = relationship("Week", back_populates="opponents")

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    court = Column(Integer)
    p1_id = Column(Integer, ForeignKey("players.id"))
    p2_id = Column(Integer, ForeignKey("players.id"))
    pairStrength = Column(Integer)
    result = Column(Integer) # (Win - 1) (Loss - 2) (Tie - 3)

    players = relationship("Player", back_populates="matches")


"""
Table Class Schema for Conversion to JSON
"""

class WeekSchema(BaseModel):
    id = int
    opp_id = int
    home_away = bool
    points = int
    delta = int

    class Config:
        from_attributes = True

