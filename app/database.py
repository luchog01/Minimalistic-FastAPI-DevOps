# app/database.py
import redis
import os
import json
from typing import Optional
from .models import Match

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

def create_match(match: Match) -> Match:
    match_id = str(redis_client.incr("match_id_counter"))
    match_data = Match(id=match_id, **match.model_dump())
    redis_client.set(f"match:{match_id}", json.dumps(match_data.model_dump()))
    return match_data

def get_matches() -> list[Match]:
    match_keys = redis_client.keys("match:*")
    matches = []
    for key in match_keys:
        match_data = json.loads(redis_client.get(key))
        matches.append(Match(**match_data))
    return matches

def get_match(match_id: str) -> Optional[Match]:
    match_data = redis_client.get(f"match:{match_id}")
    if match_data:
        return Match(**json.loads(match_data))
    return None
