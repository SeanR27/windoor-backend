from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Week(Base):
    __tablename__ = "weeks"

    id = Column(Integer, primary_key=True)
    opp_id = Column(Integer) #, ForeignKey("opponents.id")
    date_of_month = Column(Integer)
    month = Column(Integer)
    year = Column(Integer)
    home_away = Column(Boolean)
    points = Column(Integer)
    delta = Column(Integer)

    def __str__(self):
        return f"Week(ID: {self.id}, Opponent ID: {self.opp_id})"

    #opponents = relationship("Opp", back_populates="weeks")

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    court = Column(Integer)
    games_total = Column(Integer)
    position_games = Column(Integer)
    wins = Column(Integer)
    losses = Column(Integer)
    ties = Column(Integer)
    performance = Column(Integer)
    weightedScore = Column(Integer)

    def __str__(self):
        return f"Player(ID: {self.id}, Name: {self.firstName} {self.lastName})"

    #matches = relationship("Match", back_populates="players")

class Opponent(Base):
    __tablename__ = "opponents"

    id = Column(Integer, primary_key=True)
    club = Column(String)
    team = Column(String)
    matches = Column(Integer)

    def __str__(self):
        return f"Opponent(ID: {self.id}, Club: {self.club}, Team: {self.team})"

    #weeks = relationship("Week", back_populates="opponents")


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    court = Column(Integer)
    p1_id = Column(Integer, ForeignKey("players.id"))
    p2_id = Column(Integer, ForeignKey("players.id"))
    pairStrength = Column(Integer)
    result = Column(Integer) # (Win - 1) (Loss - 2) (Tie - 3)

    #players = relationship("Player", back_populates="matches")