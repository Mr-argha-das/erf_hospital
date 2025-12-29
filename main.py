from fastapi import FastAPI
from core.database import init_db
from auth.otp_routes import router
from routes.billing import router as billing_router
from routes.staffRoutes import router as staff_router
from routes.admin import router as admin_router

app = FastAPI(title="Nursing Staff Backend")

init_db()

# app.include_router(staff_router)
app.include_router(router, prefix="/auth", tags=["Authentication"])
app.include_router(billing_router, prefix="/billing", tags=["Billing"])
app.include_router(staff_router, prefix="/staff", tags=["Staff"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
