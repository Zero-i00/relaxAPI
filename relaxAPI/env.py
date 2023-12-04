from typing import Final
import os
from dotenv import load_dotenv

load_dotenv()


class BackendVariables:
    SECRET_KEY: Final = os.environ.get('DJANGO_SECRET_KEY', '')
    DEBUG: Final = os.environ.get('DEBUG', True)


class SuperUserVariables:
    NAME: Final = os.environ.get("POSTGRES_DB")
    USER: Final = os.environ.get("POSTGRES_USER")
    PASSWORD: Final = os.environ.get("POSTGRES_PASSWORD")
    HOST: Final = os.environ.get("POSTGRES_HOST")
    PORT: Final = os.environ.get("POSTGRES_PORT")