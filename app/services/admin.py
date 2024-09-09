from sqlmodel import Session

from app.models import Admin

def authenticate(*, session: Session, email: str, password: str) -> Admin | None:

