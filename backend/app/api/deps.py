from fastapi import Header, HTTPException


def require_employee_id(x_employee_id: str = Header(
        "e024",
        description="社員ID (例: e024)",
        example="e024"
    )):
    if not x_employee_id:
        raise HTTPException(status_code=400, detail="X-Employee-Id header is required")
    return x_employee_id

def require_role(x_role: str = Header(
        "user",
        description="権限 (user または admin)",
        example="user"
    )):
    if not x_role:
        raise HTTPException(status_code=400, detail="X-Role header is required")
    return x_role
