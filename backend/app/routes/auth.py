# app/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db.session import get_session
from app.core.security import create_access_token
from app.schemas.auth import Token, LoginRequest
from app.services.user_service import verify_user  # the function we wrote

router = APIRouter()


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_session)):
    user = verify_user(data.username, data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    # issue JWT token
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
