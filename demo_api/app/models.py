from pydantic import BaseModel


class Option(BaseModel):
    id: str
    text: str


class Slot(BaseModel):
    id: str
    name: str
    prompt: str
    options: list[Option]


class CaseOut(BaseModel):
    id: str
    brief: str
    slots: list[Slot]


class AttemptIn(BaseModel):
    case_id: str
    picks: dict[str, str]


class SlotResult(BaseModel):
    slot: str
    kind: str


class AttemptResult(BaseModel):
    attempt_number: int
    results: list[SlotResult]
    solved: bool


class Stats(BaseModel):
    played: int
    wins: int
    streak: int
    max_streak: int
