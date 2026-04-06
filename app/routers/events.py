from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.database import get_session
from ..cruds import events_crud as crud
from ..database.models import EventIn, EventDb

router = APIRouter(prefix="/events")



@router.get("", response_model=list[EventDb],status_code=status.HTTP_200_OK)
def get_all_events(*, session: Session = Depends(get_session)):
    return crud.get_all_events(session)

@router.get("/{event_id}", response_model=EventDb)
def get_event_by_id(*, session: Session = Depends(get_session), event_id: int):
    return crud.get_event_by_id(session, event_id)

# @router.post("", status_code=status.HTTP_201_CREATED)
# def create_event(*, session: Session = Depends(get_session), event_in: EventIn):
#     return crud.create_event(session, event_in)