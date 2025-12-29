from mongoengine import *
from datetime import datetime


class Staff(Document):
    full_name = StringField(required=True)
    phone = StringField(required=True, unique=True)
    email = EmailField()
    
    staff_type = StringField(
        choices=["GNM", "ANM", "PHYSIO", "CARE_GIVER", "COMBO"],
        required=True
    )

    aadhaar_no = StringField()
    aadhaar_verified = BooleanField(default=False)

    profile_photo = StringField()
    signature = StringField()

    qualification_docs = ListField(StringField())
    experience_docs = ListField(StringField())

    verification_status = StringField(
        choices=["PENDING", "APPROVED", "REJECTED"],
        default="PENDING"
    )

    joining_date = DateTimeField()
    base_salary = FloatField(default=0)

    is_active = BooleanField(default=True)
    created_at = DateTimeField(default=datetime.utcnow)
    otp = StringField()
    otp_expiry = DateTimeField()
    last_login = DateTimeField()

class DutyLog(Document):
    staff = ReferenceField(Staff, required=True)

    duty_type = StringField(
        choices=["DAY", "NIGHT", "24H", "VISIT"]
    )

    punch_in = DateTimeField(required=True)
    punch_out = DateTimeField()
    
    status = StringField(
        choices=["ACTIVE", "COMPLETED", "MISSED"],
        default="ACTIVE"
    )

    location = StringField()
    created_at = DateTimeField(default=datetime.utcnow)




