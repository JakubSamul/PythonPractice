from enum import Enum
from fastapi import FastAPI, Path, Query
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


card = FastAPI()


class Player(BaseModel):
    name: str | None = None
    card: list[str] | None = None

players = {}

@card.get("/get_player/{player_id}")
async def read_player(player_id: int):
    return players.get(player_id)


@card.post("/create_player/{player_id}")
async def create_player(player_id: int, player: Player):
    players[player_id] = player
    return players[player_id]


# @card.patch("/players/{player_id}", response_model=Player)
# async def patch_player(player_id: int, player: Player):
#     stored_player_data = players[player_id]
#     if stored_player_data is not None:
#         stored_player_model = Player(**stored_player_data)
#     else:
#         stored_player_model = Player()
#     update_data = player.dict(exclude_unset=True)
#     updated_player = stored_player_model.copy(update=update_data)
#     players[player_id] = jsonable_encoder(updated_player)
#     return updated_player