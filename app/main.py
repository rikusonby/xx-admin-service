from fastapi import FastAPI, Depends

from app.dependencies.api import get_token_header
from app.routers import admin

app = FastAPI(dependencies=[Depends(get_token_header)])

app.include_router(admin.router)
