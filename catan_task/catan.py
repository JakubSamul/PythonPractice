from enum import Enum
from fastapi import FastAPI, Path, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import random


card = FastAPI()


list_of_vc = [
        'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'k',
        'vp', 'vp', 'vp', 'vp', 'vp', 'v', 'v', 'v', 'br', 'br', 'br', 'm', 'm', 'm'
    ]


class Player(BaseModel):
    name: str | None = None
    cards: list[str] | None = []


players = {}


def t_card():
    take = random.choice(list_of_vc)
    list_of_vc.remove(take)
    return take

print(t_card())


@card.post("/create_player/{player_id}")
async def create_player(player_id: int, player: Player):
    players[player_id] = player
    return players[player_id]


@card.get("/get_player/{player_id}")
async def read_player(player_id: int):
    return players.get(player_id)


@card.put('/grab_card/{player_id}')
async def grab_card(player_id: int):
    player = players[player_id]
    player.cards = [t_card]
    return player