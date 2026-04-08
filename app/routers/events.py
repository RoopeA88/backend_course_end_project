from fastapi import APIRouter, status, Depends, Query
from sqlmodel import Session
from ..database.database import get_session
from ..cruds import events_crud as crud
from ..database.models import EventIn, EventDb, EventResponse
from typing import Optional

router = APIRouter(prefix="/events")



@router.get("", response_model=list[EventResponse],status_code=status.HTTP_200_OK)
def get_all_events(*, session: Session = Depends(get_session),type: Optional[str] = Query(None, description="Type of event")):
    return crud.get_all_events(session, event_type = type)



# @router.post("", status_code=status.HTTP_201_CREATED)
# def create_event(*, session: Session = Depends(get_session), event_in: EventIn):
#     return crud.create_event(session, event_in)