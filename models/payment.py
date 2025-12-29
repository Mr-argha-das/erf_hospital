from mongoengine import *
from datetime import datetime

from models.bill import Bill
from models.staff import Staff
class Payment(Document):
    bill = ReferenceField(Bill)
    amount = FloatField(required=True)

    payment_mode = StringField(
        choices=["CASH", "UPI", "CARD", "BANK"]
    )

    transaction_id = StringField()
    paid_at = DateTimeField(default=datetime.utcnow)
