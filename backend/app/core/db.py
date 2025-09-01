from sqlmodel import SQLModel, create_engine, Session
from backend.app.models.user import User
from backend.app.models.patient import Patient  # import all models here

engine = create_engine("sqlite:///mini_his.db", echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SQLModel.metadata.create_all(engine)
