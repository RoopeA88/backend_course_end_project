from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class PlayerBase(SQLModel):
    name: str
    

class PlayerIn(PlayerBase):
    pass

class PlayerDb(PlayerBase, table = True):
    id: int = Field(default=None, primary_key=True)
    events : list["EventDb"] = Relationship(back_populates="player")
    
    
class EventBase(SQLModel):
    type: str
    detail: str
    timestamp: datetime = Field(default_factory=datetime.now)
    player_id: int = Field(foreign_key="playerdb.id")

class EventIn(EventBase):
    pass

class EventDb(EventBase, table=True):
    id: int = Field(default=None, primary_key=True)
    player: PlayerDb = Relationship(back_populates="events")
    
    
class EventCreate(SQLModel):
    type: str
    detail: str
    
class PlayerReadWithEvents(PlayerBase):
    id: int
    
    events: list[EventBase] = [] 

    model_config = {"from_attributes": True}
    
class EventResponse(SQLModel):
    id: int
    type: str
    detail: str
    timestamp: datetime
    player_id: int
    