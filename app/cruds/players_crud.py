from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from ..database.models import PlayerIn, PlayerDb

def create_player(session: Session, player_in: PlayerIn):
    player = PlayerDb.model_validate(player_in)
    session.add(player)
    session.commit()
    session.refresh(player)
    return player

def get_all_players(session: Session):
    return session.exec(select(PlayerDb)).all()