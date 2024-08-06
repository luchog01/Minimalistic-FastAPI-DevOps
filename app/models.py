# app/models.py
from pydantic import BaseModel


class MatchCreate(BaseModel):
    name: str
    team1: str
    team2: str
    result: int


class Match(MatchCreate):
    id: str
