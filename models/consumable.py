from mongoengine import *
from datetime import datetime

from staff import Staff
class Consumable(Document):
    name = StringField(required=True)
    unit_price = FloatField(required=True)
    stock_qty = IntField(default=0)
