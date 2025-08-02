from fastapi import Header, HTTPException


def require_employee_id(x_employee_id: str = Header(...)):
    if not x_employee_id:
        raise HTTPException(status_code=400, detail="X-Employee-Id header is required")
    return x_employee_id
