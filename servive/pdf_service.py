from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_invoice(bill, items, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    c.drawString(50, 800, f"Invoice: {bill.bill_no}")
    y = 760
    for i in items:
        c.drawString(50, y, f"{i.item_name} x{i.quantity} = {i.total_price}")
        y -= 20
    c.drawString(50, y-20, f"Total: {bill.net_amount}")
    c.save()

def generate_payslip(salary, staff, file_path):
    c = canvas.Canvas(file_path, pagesize=A4)
    c.drawString(50, 800, f"Payslip - {staff.full_name}")
    c.drawString(50, 760, f"Net Salary: {salary.net_salary}")
    c.save()
