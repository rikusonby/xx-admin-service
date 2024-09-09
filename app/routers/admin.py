from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta
from typing import Annotated, Any

from app.dependencies.database import SessionDB
from app.models import Token

router = APIRouter()


@router.post("/admin/login", tags=["admin"])
async def admin_login(session: SessionDB, form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    return Token()
