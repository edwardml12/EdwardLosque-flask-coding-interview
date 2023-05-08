from typing import Optional

from pydantic import BaseModel

from flask_openapi3 import APIBlueprint
from sqlalchemy import select

from database import db
from api.users.models import Users

users_app = APIBlueprint("users_app", __name__)


class UserSchema(BaseModel):
    id: int
    password: str
    email: str
    created_at: str
    updated_at: str
    last_login: str
    first_name: str
    last_name: str


class UserList(BaseModel):
    users: list[UserSchema]


@users_app.get("/users", responses={"200": UserList})
def get_users():
    with db.session() as session:
        users = session.execute(select(Users)).scalars().all()
        return users
