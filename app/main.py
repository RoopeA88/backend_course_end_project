from fastapi import FastAPI
from .routers import players, events, players_events
from contextlib import asynccontextmanager
from .database.database import create_db
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
    
)

app.include_router(players.router)
app.include_router(events.router)
app.include_router(players_events.router)


