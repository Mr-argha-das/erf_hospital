from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from datetime import datetime
from models.staff import Staff, DutyLog
from models.leave import LeaveRequest
from models.salary import SalarySlip
from models.sos import SOS
from models.staff_id import StaffID
from auth.auth import get_current_user
from models.visit import Visit

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.post("/apply")
def apply_staff(data: dict):
    staff = Staff(**data)
    staff.verification_status = "PENDING"
    staff.save()
    return {"msg": "Application submitted", "id": str(staff.id)}
@router.post("/{staff_id}/upload/{doc_type}")
def upload_doc(staff_id: str, doc_type: str, file: UploadFile = File(...)):
    staff = Staff.objects(id=staff_id).first()
    if not staff:
        raise HTTPException(404, "Staff not found")

    if doc_type == "qualification":
        staff.qualification_docs.append(file.filename)
    elif doc_type == "experience":
        staff.experience_docs.append(file.filename)

    staff.save()
    return {"msg": "Document uploaded"}
@router.post("/{staff_id}/profile-photo")
def upload_photo(staff_id: str, file: UploadFile = File(...)):
    Staff.objects(id=staff_id).update(profile_photo=file.filename)
    return {"msg": "Profile photo uploaded"}

@router.post("/{staff_id}/signature")
def upload_signature(staff_id: str, file: UploadFile = File(...)):
    Staff.objects(id=staff_id).update(signature=file.filename)
    return {"msg": "Signature saved"}
@router.post("/{staff_id}/profile-photo")
def upload_photo(staff_id: str, file: UploadFile = File(...)):
    Staff.objects(id=staff_id).update(profile_photo=file.filename)
    return {"msg": "Profile photo uploaded"}

@router.post("/{staff_id}/signature")
def upload_signature(staff_id: str, file: UploadFile = File(...)):
    Staff.objects(id=staff_id).update(signature=file.filename)
    return {"msg": "Signature saved"}
@router.post("/{staff_id}/punch-in")
def punch_in(staff_id: str, location: str):
    DutyLog(
        staff=staff_id,
        punch_in=datetime.utcnow(),
        location=location
    ).save()
    return {"msg": "Duty started"}

@router.post("/{staff_id}/punch-out")
def punch_out(staff_id: str):
    duty = DutyLog.objects(staff=staff_id, status="ACTIVE").first()
    if not duty:
        raise HTTPException(400, "No active duty")

    duty.update(punch_out=datetime.utcnow(), status="COMPLETED")
    return {"msg": "Duty closed"}
@router.post("/{staff_id}/leave")
def apply_leave(staff_id: str, data: dict):
    LeaveRequest(staff=staff_id, **data).save()
    return {"msg": "Leave requested"}
@router.post("/{staff_id}/sos")
def sos(staff_id: str, message: str):
    SOS(staff=staff_id, message=message).save()
    return {"msg": "SOS sent"}
@router.get("/{staff_id}/visits")
def staff_visits(staff_id: str):
    return list(Visit.objects(staff=staff_id))
