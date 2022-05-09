from fastapi import FastAPI

from routes import user_route

app = FastAPI(
    title="Users API",
    description="Users management",
    version="0.0.1",
    openapi_tags=[{
        'name': 'user',
        'description': 'User routes'
    }]
)

app.include_router(user_route)
