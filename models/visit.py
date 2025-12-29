from mongoengine import *
from datetime import datetime

from models.staff import Staff

class Visit(Document):
    staff = ReferenceField(Staff)
    patient_name = StringField(required=True)
    patient_phone = StringField()
    address = StringField()

    visit_time = DateTimeField()
    visit_notes = StringField()

    completed = BooleanField(default=False)
