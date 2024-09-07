from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", tags=["users"])
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.post("/user/login", tags=["users"])
async def user_login(username: str, password: str):
    return {"username": username, "password": password}
