from fastapi import FastAPI, Depends

from app.core.config import settings
from .dependencies import get_token_header, get_query_token
from .internal import admin
from .routers import items, users


app = FastAPI(dependencies=[Depends(get_token_header)])

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello " + settings.app_name}
