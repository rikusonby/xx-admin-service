from fastapi import APIRouter, Depends

from datetime import timedelta
from typing import Annotated, Any

router = APIRouter()


@router.post("/admin/login", tags=["admin"])
async def admin_login(username: str, password: str):
    return {"status": "ok"}
