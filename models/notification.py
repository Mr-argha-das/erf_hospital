from mongoengine import *
from datetime import datetime

from staff import Staff
class Notification(Document):
    title = StringField()
    message = StringField()
    user_type = StringField(
        choices=["ADMIN", "STAFF", "DOCTOR"]
    )
    is_read = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.utcnow)
