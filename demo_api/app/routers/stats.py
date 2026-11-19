from fastapi import APIRouter

from ..models import Stats

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/me", response_model=Stats)
def my_stats() -> Stats:
    return Stats(played=0, wins=0, streak=0, max_streak=0)
