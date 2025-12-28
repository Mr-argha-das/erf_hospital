from fastapi import APIRouter, UploadFile, File
from modules.staff.models import *
from utils.file_upload import save_file
from datetime import datetime
import uuid

staff_router = APIRouter(prefix="/staff", tags=["Staff"])
@staff_router.post("/apply")
def apply_staff(data: dict):
    staff = Staff(**data)
    staff.save()
    return {"msg": "Application submitted", "id": str(staff.id)}
@staff_router.post("/{staff_id}/upload-doc")
def upload_doc(staff_id: str, file: UploadFile = File(...)):
    staff = Staff.objects(id=staff_id).first()
    path = save_file(file, "documents")
    staff.qualification_docs.append(path)
    staff.save()
    return {"msg": "Uploaded"}
@staff_router.post("/{staff_id}/photo")
def upload_photo(staff_id: str, file: UploadFile = File(...)):
    staff = Staff.objects(id=staff_id).first()
    staff.profile_photo = save_file(file, "profiles")
    staff.save()
    return {"msg": "Photo uploaded"}
@staff_router.post("/{staff_id}/signature")
def upload_signature(staff_id: str, file: UploadFile = File(...)):
    staff = Staff.objects(id=staff_id).first()
    staff.signature = save_file(file, "signature")
    staff.save()
    return {"msg": "Signature saved"}
@staff_router.get("/{staff_id}")
def get_staff(staff_id: str):
    staff = Staff.objects(id=staff_id).first()
    return staff.to_mongo()
@staff_router.post("/{staff_id}/punch-in")
def punch_in(staff_id: str, duty_type: str):
    duty = DutyLog(
        staff=staff_id,
        duty_type=duty_type,
        punch_in=datetime.utcnow()
    )
    duty.save()
    return {"msg": "Duty started"}
@staff_router.post("/{staff_id}/punch-out")
def punch_out(staff_id: str):
    duty = DutyLog.objects(staff=staff_id, status="ACTIVE").first()
    duty.punch_out = datetime.utcnow()
    duty.status = "COMPLETED"
    duty.save()
    return {"msg": "Duty closed"}
@staff_router.post("/{staff_id}/visit")
def create_visit(staff_id: str, data: dict):
    visit = Visit(staff=staff_id, **data)
    visit.save()
    return {"msg": "Visit scheduled"}
@staff_router.post("/{staff_id}/sos")
def sos(staff_id: str, message: str):
    sos = SOS(staff=staff_id, message=message)
    sos.save()
    return {"msg": "SOS sent"}
@staff_router.post("/{staff_id}/id-card")
def generate_id(staff_id: str):
    card = StaffID(
        staff=staff_id,
        card_no=str(uuid.uuid4())[:8]
    )
    card.save()
    return {"card_no": card.card_no}
