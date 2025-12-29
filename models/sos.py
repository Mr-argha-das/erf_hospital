from mongoengine import *
from datetime import datetime
from models.staff import Staff

class SOS(Document):
    staff = ReferenceField(Staff)
    message = StringField()
    emergency_level = StringField(
        choices=["LOW", "MEDIUM", "HIGH"],
        default="HIGH"
    )
    created_at = DateTimeField(default=datetime.utcnow)
