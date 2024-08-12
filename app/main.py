# app/main.py
# Author: Luciano Garbarino 2024
from fastapi import FastAPI, HTTPException
from .models import MatchCreate, Match
from . import database

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"status": "ok"}


@app.post("/matches", response_model=Match)
async def create_match(match: MatchCreate):
    return database.create_match(match)


@app.get("/matches", response_model=list[Match])
async def get_matches():
    return database.get_matches()


@app.get("/matches/{match_id}", response_model=Match)
async def get_match(match_id: str):
    match = database.get_match(match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match
