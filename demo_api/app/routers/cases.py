from fastapi import APIRouter, HTTPException
import random

from ..models import CaseOut

router = APIRouter(prefix="/cases", tags=["cases"])

CASES: dict[str, CaseOut] = {}


@router.get("/today", response_model=CaseOut)
def today_case() -> CaseOut:
    """The case everyone plays today."""
    if not CASES:
        raise HTTPException(404, "No cases loaded")
    return next(iter(CASES.values()))


@router.get("/random", response_model=CaseOut)
def random_case(exclude: str | None = None) -> CaseOut:
    """A practice case, never the one passed in `exclude`."""
    pool = [c for cid, c in CASES.items() if cid != exclude]
    if not pool:
        raise HTTPException(404, "No practice cases")
    return random.choice(pool)


@router.get("/{case_id}", response_model=CaseOut)
def get_case(case_id: str) -> CaseOut:
    if case_id not in CASES:
        raise HTTPException(404, "Unknown case")
    return CASES[case_id]
