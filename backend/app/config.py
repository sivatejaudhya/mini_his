import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Mini-HIS"
    VERSION: str = "1.0.0"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "defaultsecret")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

# Create a single settings object to import anywhere
settings = Settings()
