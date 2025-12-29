from mongoengine import *
from datetime import datetime
from models.staff import Staff


class StaffID(Document):
    staff = ReferenceField(Staff, required=True)
    card_no = StringField(unique=True)
    issued_at = DateTimeField(default=datetime.utcnow)
    is_active = BooleanField(default=True)
