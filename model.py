


from enum import Enum
from secrets import token_hex
from typing import Dict, List, Optional, Union

import mongoengine as me
from bson import ObjectId
from typeguard import typechecked

import uuid
from typing import Optional
from pydantic import BaseModel, Field

class User(me.Document):
    id = me.StringField(primary_key=True)
    name = me.StringField()
    email = me.EmailField()

    @classmethod
    def create_from_(cls, data: Dict) -> "User":
        return cls(**data).save()


class Entry(me.Document):
    id = me.ObjectIdField(primary_key=True, default=ObjectId)
    user_id = me.ReferenceField(User)
    title = me.StringField()
    content = me.StringField()
    image = me.URLField()
    mood = me.StringField()
    date = me.StringField()
    activities = me.ListField(me.StringField())
    feelings = me.ListField(me.DictField())
    created_at = me.DateTimeField(auto_now_add=True)
    updated_at = me.DateTimeField(auto_now=True)

    @classmethod
    def create_from_(cls, data: Dict) -> "Entry":
        return cls(**data).save()


class ConversationTranscript(me.Document):
    id = me.ObjectIdField(primary_key=True, default=ObjectId)
    session_id = me.StringField(default=token_hex(16), unique=True)
    raw = me.DictField()

    @classmethod
    def create_from_(cls, transcript:Dict):
        return cls(raw=transcript, session_id=transcript.get('session_id')).save()

if __name__ == "__main__":
    from config import *
    ConversationTranscript.create_from_({"session_id": "XXXX"})