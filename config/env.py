import os
from dotenv import load_dotenv
from pathlib import Path


__dir = os.path.dirname(__file__)
__path = os.path.join(__dir, '..', '.env')
__dotenv_path = Path(__path).resolve()

load_dotenv(dotenv_path=__dotenv_path)


ConnectionDBOptions = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_UID'),
    'password': os.getenv('DB_PWD'),
    'database': os.getenv('DB_DB')
}
