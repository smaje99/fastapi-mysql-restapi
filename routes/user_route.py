from cryptography.fernet import Fernet
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT

from config.database import connection as conn
from models import User as model
from schemas import User


__key = Fernet.generate_key()
__func = Fernet(__key)

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get('/{id}', response_model=User)
async def get_user(id: int):
    result = (conn.execute(
        model
        .select()
        .where(model.c.id == id)
    ).first())

    return result


@router.get('/', response_model=list[User])
async def get_users():
    result = (conn.execute(model.select)
              .fetchall())
    return result


@router.post('/', response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
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


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
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


@router.put('/{id}', response_model=User)
async def update_user(id: int, user: User):
    (conn.execute(
        model
        .update()
        .values(
            name=user.name,
            email=user.email,
            password=__func.encrypt(user.password.encode('utf-8'))
        )
        .where(model.c.user_id == id)
    ))

    user_updated = (conn.execute(
        model
        .select()
        .where(model.c.user_id == id)
    ).first())

    return user_updated
