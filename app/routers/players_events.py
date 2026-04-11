from fastapi import APIRouter, status, Depends, Query
from sqlmodel import Session
from ..database.database import get_session
from ..cruds import events_crud as crud
from ..database.models import EventCreate, EventDb, EventResponse
from typing import Optional

router = APIRouter(prefix="/players/{id}/events")

@router.post("", status_code=status.HTTP_201_CREATED, response_model = EventResponse)
def create_event(*, session: Session = Depends(get_session), event_in: EventCreate, id: int):
    return crud.create_event(session, event_in, id)

@router.get("", response_model=list[EventResponse])
def get_events_by_player_id(*, session: Session = Depends(get_session), player_id: int, type: Optional[str] = Query(None, description="Type of event")):
    return crud.get_events_by_player_id(session, player_id, event_type = type)