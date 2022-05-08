import os
from dotenv import load_dotenv
from pathlib import Path


__dir = os.path.dirname(__file__)
__path = os.path.join(__dir, '..', '.env')
__dotenv_path = Path(__path).resolve()

load_dotenv(dotenv_path=__dotenv_path)
