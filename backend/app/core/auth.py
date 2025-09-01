from fastapi import HTTPException, status
from sqlmodel import Session, select
from app.models.user import User
from app.core.security import verify_password  # your hash checker


def verify_user(username: str, password: str, db: Session) -> User:
    try:
        # Query user from DB
        statement = select(User).where(User.username == username)
        user = db.exec(statement).first()

        # If user not found or password doesn’t match
        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password",
            )

        return user

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error",
        )
