# FILE: /fastapi-diary-app/fastapi-diary-app/src/types/__init__.py
# This file can define any custom types or interfaces used throughout the application, ensuring type safety and clarity in the data structures.

from typing import List, Dict, Any

Transcript = Dict[str, Any]
Summary = str
TitleWithEmoji = str
MoodAnalysis = str
ActivitiesList = List[str]
Reflections = str

class DiaryEntry:
    def __init__(self, summary: Summary, title: TitleWithEmoji, mood: MoodAnalysis, activities: ActivitiesList, reflections: Reflections):
        self.summary = summary
        self.title = title
        self.mood = mood
        self.activities = activities
        self.reflections = reflections