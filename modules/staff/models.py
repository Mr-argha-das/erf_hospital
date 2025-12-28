from mongoengine import *
from datetime import datetime

class Staff(Document):
    full_name = StringField(required=True)
    phone = StringField(required=True, unique=True)
    staff_type = StringField(choices=["GNM","ANM","PHYSIO","CARE_GIVER","COMBO"])

    aadhaar_verified = BooleanField(default=False)

    profile_photo = StringField()
    signature = StringField()

    qualification_docs = ListField(StringField())
    experience_docs = ListField(StringField())

    verification_status = StringField(default="PENDING")
    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)

class DutyLog(Document):
    staff = ReferenceField(Staff)
    duty_type = StringField()
    punch_in = DateTimeField()
    punch_out = DateTimeField()
    status = StringField(default="ACTIVE")
    date = DateTimeField(default=datetime.utcnow)

class Visit(Document):
    staff = ReferenceField(Staff)
    patient_name = StringField()
    address = StringField()
    visit_time = DateTimeField()
    completed = BooleanField(default=False)

class SOS(Document):
    staff = ReferenceField(Staff)
    message = StringField()
    created_at = DateTimeField(default=datetime.utcnow)

class StaffID(Document):
    staff = ReferenceField(Staff)
    card_no = StringField(unique=True)
    issued_at = DateTimeField(default=datetime.utcnow)
