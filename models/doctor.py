from mongoengine import *
from datetime import datetime

from models.staff import Staff

class Doctor(Document):
    full_name = StringField(required=True)
    phone = StringField(unique=True)
    email = EmailField()

    specialization = StringField(required=True)
    registration_no = StringField()

    consultation_fee = FloatField(default=0)

    available_days = ListField(
        StringField(choices=["MON","TUE","WED","THU","FRI","SAT","SUN"])
    )
    available_from = StringField()
    available_to = StringField()

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    otp = StringField()
    otp_expiry = DateTimeField()
    last_login = DateTimeField()
