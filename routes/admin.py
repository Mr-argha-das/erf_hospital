from fastapi import APIRouter
from datetime import datetime
from models.staff import Staff
from models.leave import LeaveRequest
from models.salary import SalarySlip
from models.staff_id import StaffID
from models.bill import Bill
from models.staff  import DutyLog

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.put("/staff/{staff_id}/verify")
def verify_staff(staff_id: str, status: str):
    Staff.objects(id=staff_id).update(verification_status=status)
    return {"msg": "Verification updated"}
@router.post("/staff/{staff_id}/id-card")
def generate_id(staff_id: str):
    StaffID(staff=staff_id, card_no=f"STAFF-{staff_id[:6]}").save()
    return {"msg": "ID card generated"}
@router.put("/leave/{leave_id}")
def approve_leave(leave_id: str, status: str):
    LeaveRequest.objects(id=leave_id).update(status=status)
    return {"msg": "Leave updated"}
@router.post("/salary/generate")
def generate_salary(staff_id: str, data: dict):
    net = data["basic_salary"] + data.get("allowances",0) - data.get("deductions",0)
    SalarySlip(staff=staff_id, net_salary=net, **data).save()
    return {"msg": "Salary generated"}
@router.get("/dashboard")
def dashboard():
    return {
        "total_staff": Staff.objects.count(),
        "active_duty": DutyLog.objects(status="ACTIVE").count(),
        "pending_verification": Staff.objects(verification_status="PENDING").count(),
        "today_billing": Bill.objects.count()
    }
