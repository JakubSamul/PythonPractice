from enum import Enum
from fastapi import FastAPI, Path, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


card = FastAPI()


class Card(BaseModel):
    cards: list[str] = [
        'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k',
        'vp', 'vp', 'vp', 'vp', 'vp', 'v', 'v', 'v', 'br', 'br', 'br', 'm', 'm', 'm'
    ]


class Player(BaseModel):
    name: str | None = None
    card: list[str] | None = None


players = {}

def grab_card(player_id: int, card: Card):
    pass

@card.get("/get_player/{player_id}")
async def read_player(player_id: int):
    return players.get(player_id)


@card.post("/create_player/{player_id}")
async def create_player(player_id: int, player: Player):
    players[player_id] = player
    return players[player_id]

