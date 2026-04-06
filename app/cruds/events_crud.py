from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from ..database.models import EventIn, EventDb, EventIn, EventCreate, PlayerDb

event_types = ["level_started", "level_solved"]

def create_event(session: Session, event_in: EventCreate, id: int):
    event = EventDb.model_validate(event_in, update={"player_id": id})
    player = session.get(PlayerDb, id)
    
    if not player:
        raise HTTPException(detail = "player not found", status_code=status.HTTP_404_NOT_FOUND)
    
    if event.type not in event_types:
        raise HTTPException(detail = "unrecognizable event", status_code=status.HTTP_400_BAD_REQUEST)
    
    event.player = player
    
    session.add(event)
    session.commit()
    session.refresh(event)
    return event

def get_all_events(session: Session):
    return session.exec(select(EventDb)).all()

def get_event_by_id(session: Session, event_id: int):
    event = session.get(EventDb, event_id)
    if not event:
        raise HTTPException(detail="event not found", status_code=status.HTTP_404_NOT_FOUND)
    
    return event