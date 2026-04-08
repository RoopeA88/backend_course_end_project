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

def get_all_events(session: Session, event_type = None):
    query = select(EventDb)
    if event_type:
        if event_type not in event_types:
            raise HTTPException(detail = "unrecognizable event", status_code=status.HTTP_400_BAD_REQUEST)
        else:
            query = query.where(EventDb.type == event_type)
    return session.exec(query).all()

def get_events_by_player_id(session: Session, player_id: int):
    query = select(EventDb).where(EventDb.player_id == player_id)
    events = session.exec(query).all()
    if not events:
        raise HTTPException(detail="event not found", status_code=status.HTTP_404_NOT_FOUND)
    
    return events