from fastapi import APIRouter

router = APIRouter()


@router.post("/admin/login", tags=["admin"])
async def admin_login(username: str, password: str):
    return {"status": "ok"}
