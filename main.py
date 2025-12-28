from fastapi import FastAPI
from core.database import init_db
from modules.staff.routes import staff_router
from auth.otp_routes import otp_router

app = FastAPI(title="Nursing Staff Backend")

init_db()

app.include_router(staff_router)
app.include_router(otp_router)
