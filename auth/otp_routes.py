from fastapi import APIRouter, Depends
from auth.auth import get_current_user
from models.doctor import Doctor
from models.staff import Staff
from fastapi import APIRouter, HTTPException

from datetime import datetime, timedelta
import random, jwt

router = APIRouter()
SECRET = "SECRET_KEY"
ADMIN_PHONE = "9999999999"
ADMIN_PASSWORD = "admin123"

@router.post("/send-otp")
def send_otp(phone: str, user_type: str):
    otp = str(random.randint(100000, 999999))
    expiry = datetime.utcnow() + timedelta(minutes=5)

    if user_type == "STAFF":
        user = Staff.objects(phone=phone, is_active=True).first()
    elif user_type == "DOCTOR":
        user = Doctor.objects(phone=phone, is_active=True).first()
    else:
        raise HTTPException(400, "Invalid user type")

    if not user:
        raise HTTPException(404, "User not found")

    user.update(otp=otp, otp_expiry=expiry)

    print("OTP:", otp)  # SMS gateway here
    return {"message": "OTP sent"}
@router.post("/verify-otp")
def verify_otp(phone: str, otp: str, user_type: str):
    if user_type == "STAFF":
        user = Staff.objects(phone=phone).first()
    elif user_type == "DOCTOR":
        user = Doctor.objects(phone=phone).first()
    else:
        raise HTTPException(400, "Invalid user type")

    if not user or user.otp != otp:
        raise HTTPException(400, "Invalid OTP")

    if user.otp_expiry < datetime.utcnow():
        raise HTTPException(400, "OTP expired")

    token = jwt.encode(
        {
            "id": str(user.id),
            "type": user_type
        },
        SECRET,
        algorithm="HS256"
    )

    user.update(
        otp=None,
        otp_expiry=None,
        last_login=datetime.utcnow()
    )

    return {
        "token": token,
        "user_type": user_type,
        "id": str(user.id)
    }
@router.post("/admin-login")
def admin_login(phone: str, password: str):
    if phone != ADMIN_PHONE or password != ADMIN_PASSWORD:
        raise HTTPException(401, "Invalid admin credentials")

    token = jwt.encode(
        {"type": "ADMIN"},
        SECRET,
        algorithm="HS256"
    )

    return {"token": token}
@router.get("/secure")
def secure_api(user=Depends(get_current_user)):
    return {"msg": "Authorized", "user": user}