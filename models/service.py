from mongoengine import *
from datetime import datetime

from staff import Staff
class Service(Document):
    name = StringField(required=True)
    category = StringField(
        choices=["CONSULTATION", "PROCEDURE", "LAB", "OTHER"]
    )
    price = FloatField(required=True)
    is_active = BooleanField(default=True)
