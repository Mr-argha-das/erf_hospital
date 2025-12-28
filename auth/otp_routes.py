from fastapi import APIRouter
from modules.staff.models import Staff

otp_router = APIRouter(prefix="/otp", tags=["OTP"])

@otp_router.post("/verify")
def verify_otp(phone: str, otp: str):
    if otp != "123456":
        return {"error": "Invalid OTP"}
    staff = Staff.objects(phone=phone).first()
    staff.aadhaar_verified = True
    staff.save()
    return {"msg": "Verified"}
