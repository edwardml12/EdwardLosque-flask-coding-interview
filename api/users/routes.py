from typing import Optional

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel
from sqlalchemy import select

from api.users.models import Users
from database import db

users_app = APIBlueprint("users_app", __name__)


class UserSchema(BaseModel):
    id: int
    password: str
    email: str
    created_at: str
    updated_at: str
    last_login: Optional[str]
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    password: str
    email: str
    first_name: str
    last_name: str


class UserList(BaseModel):
    users: list[UserSchema]

class User(BaseModel):
    user: UserSchema


@users_app.get("/users", responses={"200": UserList})
def get_users():
    with db.session() as session:
        users_query = session.execute(select(Users)).scalars().all()
        users_list = [UserSchema.from_orm(user).dict() for user in users_query]
        return {"users": users_list}


@users_app.post("/users", responses={"201": UserSchema})
def create_user(body: UserCreateSchema):
    with db.session() as session:
        new_user = Users(
            password=body.password,
            email=body.email,
            first_name=body.first_name,
            last_name=body.last_name,
            created_at="now",
            updated_at="now",
            last_login=None,
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return UserSchema.from_orm(new_user).dict(), 201


@users_app.get(
    "/users/<int:user_id>",
    responses={"200": User, "404": None},
)
def get_user(user_id: int):
    with db.session() as session:
        user = session.get(Users, user_id)
        return UserSchema.from_orm(user).dict()


@users_app.delete("/users/<int:user_id>", responses={"204": None, "404": None})
def delete_user(user_id: int):
    with db.session() as session:
        user = session.get(Users, user_id)
        if not user:
            return {"message": "User not found"}, 404
        session.delete(user)
        session.commit()
        return "", 204
