from cryptography import Fernet
from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

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
        .where(model.c.id == id)
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


@router.delete('/user/{id}')
def delete_user(id):
    """
    It deletes a user from the database

    :param id: The id of the user to delete
    :return: The first row of the result set.
    """
    (conn.execute(
        model
        .delete()
        .where(model.c.id == id)
    ))

    return Response(status_code=HTTP_204_NO_CONTENT)
