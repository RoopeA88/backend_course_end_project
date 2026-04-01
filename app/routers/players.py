from fastapi import APIRouter, status

router = APIRouter(prefix="/players")

players = [{"id": 0, "name": "roope"},
        {"id": 1, "name": "matias"}]

@router.get("",status_code=status.HTTP_200_OK)
def get_all_players():
    return players