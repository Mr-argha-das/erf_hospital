from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, ReferenceField, IntField, FloatField

from models.staff import Staff
class SalarySlip(Document):
    staff = ReferenceField(Staff, required=True)

    month = IntField(min_value=1, max_value=12)
    year = IntField()

    basic_salary = FloatField()
    allowances = FloatField(default=0)
    deductions = FloatField(default=0)

    net_salary = FloatField()
    generated_at = DateTimeField(default=datetime.utcnow)

    payment_status = StringField(
        choices=["PENDING", "PAID"],
        default="PENDING"
    )
