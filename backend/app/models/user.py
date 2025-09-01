from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(..., unique=True)
    email: str = Field(..., unique=True)
    password: str
    role: str
