
from mongoengine import *
from datetime import datetime

from models.doctor import Doctor
from models.staff import Staff

class Bill(Document):
    bill_no = StringField(unique=True)

    patient_name = StringField(required=True)
    patient_phone = StringField()

    doctor = ReferenceField(Doctor)
    created_by_staff = ReferenceField(Staff)

    total_amount = FloatField()
    discount = FloatField(default=0)
    net_amount = FloatField()

    status = StringField(
        choices=["PENDING", "PAID", "CANCELLED"],
        default="PENDING"
    )

    created_at = DateTimeField(default=datetime.utcnow)
