from mongoengine import *
from datetime import datetime

from models.bill import Bill
from models.staff import Staff
class BillItem(Document):
    bill = ReferenceField(Bill, required=True)

    item_type = StringField(
        choices=["SERVICE", "CONSUMABLE"]
    )

    item_name = StringField()
    quantity = IntField(default=1)
    unit_price = FloatField()
    total_price = FloatField()
