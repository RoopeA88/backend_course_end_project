from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.database import get_session
from ..cruds import players_crud as crud
from ..database.models import PlayerIn, PlayerDb, PlayerReadWithEvents

router = APIRouter(prefix="/players")



@router.get("", response_model=list[PlayerDb],status_code=status.HTTP_200_OK)
def get_all_players(*, session: Session = Depends(get_session)):
    return crud.get_all_players(session)

@router.get("/{player_id}", response_model=PlayerReadWithEvents, responses={ 404: {"description": "player not found"}}, status_code=status.HTTP_200_OK)
def get_player_by_id(*, session: Session = Depends(get_session), player_id: int):
    return crud.get_player_by_id(session, player_id)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=PlayerDb)
def create_player(*, session: Session = Depends(get_session), player_in: PlayerIn):
    return crud.create_player(session, player_in)