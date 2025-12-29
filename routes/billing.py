from fastapi import APIRouter, HTTPException
from models.bill import Bill
from models.bill_item import BillItem
from models.payment import Payment
import uuid

router = APIRouter(prefix="/billing", tags=["Billing"])
@router.post("/")
def create_bill(data: dict):
    bill = Bill(
        bill_no=str(uuid.uuid4())[:8],
        patient_name=data["patient_name"],
        patient_phone=data.get("patient_phone"),
        doctor=data.get("doctor"),
        created_by_staff=data.get("staff"),
        total_amount=0,
        net_amount=0
    )
    bill.save()
    return {"bill_id": str(bill.id)}
@router.post("/{bill_id}/item")
def add_item(bill_id: str, data: dict):
    bill = Bill.objects(id=bill_id).first()
    if not bill:
        raise HTTPException(404, "Bill not found")

    total = data["quantity"] * data["unit_price"]
    BillItem(bill=bill, total_price=total, **data).save()

    bill.total_amount += total
    bill.net_amount = bill.total_amount - bill.discount
    bill.save()

    return {"msg": "Item added"}
@router.post("/{bill_id}/payment")
def payment(bill_id: str, data: dict):
    bill = Bill.objects(id=bill_id).first()
    Payment(bill=bill, **data).save()
    return {"msg": "Payment recorded"}
