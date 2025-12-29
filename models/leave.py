from datetime import datetime
from mongoengine import Document, StringField, DateTimeField, ReferenceField

from models.staff import Staff


class LeaveRequest(Document):
    staff = ReferenceField(Staff, required=True)

    leave_type = StringField(
        choices=["CASUAL", "SICK", "EMERGENCY"]
    )

    from_date = DateTimeField(required=True)
    to_date = DateTimeField(required=True)

    reason = StringField()

    status = StringField(
        choices=["PENDING", "APPROVED", "REJECTED"],
        default="PENDING"
    )

    approved_by = StringField()
    applied_at = DateTimeField(default=datetime.utcnow)
