from fastapi import APIRouter, HTTPException

from ..models import CaseOut

router = APIRouter(prefix="/cases", tags=["cases"])

CASES: dict[str, CaseOut] = {}


@router.get("/today", response_model=CaseOut)
def today_case() -> CaseOut:
    """The case everyone plays today."""
    if not CASES:
        raise HTTPException(404, "No cases loaded")
    return next(iter(CASES.values()))


@router.get("/{case_id}", response_model=CaseOut)
def get_case(case_id: str) -> CaseOut:
    if case_id not in CASES:
        raise HTTPException(404, "Unknown case")
    return CASES[case_id]
