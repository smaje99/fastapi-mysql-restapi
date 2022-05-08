from cryptography import Fernet
from fastapi import APIRouter

from config.database import connection as conn
from models import User as model
from schemas import User


__key = Fernet.generate_key()
__func = Fernet(__key)

router = APIRouter()


@router.get('/user/{id}')
def get_user(id: int):
    result = (conn.execute(
        model
        .select()
        .where(model.User.id == id)
    ).first())

    return result


@router.get('/users')
def get_users():
    result = (conn.execute(model.select)
              .fetchall())
    return result


@router.post('/user')
def create_user(user: User):
    new_user = {
        'name': user.name,
        'email': user.email,
        'password': __func.encrypt(user.password.encode('utf-8')),
    }

    result = conn.execute(model.insert().values(new_user))
    user_created = (conn.execute(
        model
        .select()
        .where(model.c.id == result.lastrowid)
    ).first())

    return user_created
