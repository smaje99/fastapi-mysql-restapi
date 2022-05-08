from fastapi import APIRouter

from config.database import connection as conn
from models import User


router = APIRouter()

@router.get('/users')
def get_users():
    result = (conn.execute(User.select)
              .fetchall())
    return result
