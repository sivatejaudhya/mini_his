from sqlmodel import SQLModel, Field


class Patient(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    age: int
    gender: str
    contact: str = None
    address: str = None
    medical_record_id: str = Field(..., unique=True)
