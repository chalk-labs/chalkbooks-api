from pydantic import BaseModel
from typing import List, Optional

class DiaryEntry(BaseModel):
    summary: str
    title: str
    emoji: str
    mood: str
    activities: List[str]
    reflections: Optional[str] = None