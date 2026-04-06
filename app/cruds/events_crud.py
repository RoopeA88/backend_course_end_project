from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from ..database.models import EventIn, EventDb

def create_event(session: Session, event_in: EventIn):
    event = EventDb.model_validate(event_in)
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