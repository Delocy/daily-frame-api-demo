from fastapi import APIRouter

from ..models import AttemptIn, AttemptResult, SlotResult

router = APIRouter(prefix="/attempts", tags=["attempts"])


@router.post("", response_model=AttemptResult, status_code=201)
def submit_attempt(body: AttemptIn) -> AttemptResult:
    """Score one attempt: one result per slot."""
    results = [SlotResult(slot=slot, kind="wrong") for slot in body.picks]
    return AttemptResult(attempt_number=1, results=results, solved=False)
