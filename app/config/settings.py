import os
from pathlib import Path
from dataclasses import dataclass

from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)




@dataclass
class Settings:
    TITTLE: str = "Bus Location API"
    VERSION: str = "1.0.0"

    IS_DEV: bool = os.getenv("IS_DEV", False)
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD")
    MONGO_HOST: str = os.getenv("MONGO_HOST")
    MONGO_PORT: str = os.getenv("MONGO_PORT")
    DB_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"


settings = Settings()
print(settings.DB_URL)
print(settings.MONGO_HOST)