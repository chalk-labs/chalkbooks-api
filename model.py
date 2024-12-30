


from enum import Enum
from secrets import token_hex
from typing import Dict, Optional, Union

import mongoengine as me
from bson import ObjectId
from typeguard import typechecked



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