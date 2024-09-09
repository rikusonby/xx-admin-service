from collections.abc import Generator
from fastapi import Depends
from typing import Annotated
from sqlmodel import Session

from app.core.db import engine


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDB = Annotated[Session, Depends(get_db)]
