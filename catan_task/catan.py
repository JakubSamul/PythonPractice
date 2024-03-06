import random

from fastapi import FastAPI
from pydantic import BaseModel

card = FastAPI()


list_of_vc = [
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "k",
    "vp",
    "vp",
    "vp",
    "vp",
    "vp",
    "v",
    "v",
    "v",
    "br",
    "br",
    "br",
    "m",
    "m",
    "m",
]


class Player(BaseModel):
    name: str | None = None
    cards: list[str] = []


players = {}


@card.post("/create_player/{player_id}")
async def create_player(player_id: int, player: Player):
    players[player_id] = player
    return players[player_id]


@card.get("/get_VCard")
async def read_vcards():
    return list_of_vc


@card.get("/get_player/{player_id}")
async def read_player(player_id: int):
    return players.get(player_id)


@card.post("/grab_card/{player_id}")
async def grab_card(player_id: int):
    player = players[player_id]
    if len(list_of_vc) == 0:
        return "Brak kard rozwoju"
    else:
        take = random.choice(list_of_vc)
        list_of_vc.remove(take)
        player.cards.append(take)
    return player
