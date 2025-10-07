from typing import Optional

from flask_openapi3 import APIBlueprint
from pydantic import BaseModel
from sqlalchemy import select

from api.users.models import Students
from database import db

students_app = APIBlueprint("students_app", __name__)

class StudentSchema(BaseModel):
    id: int
    user_id: str
    enrollment_date: str
    created_at: str
    min_course_credits: str

    class Config:
        orm_mode = True


class StudentCreateSchema(BaseModel):
    enrollment_date: str
    min_course_credits: str
    user_id: str


class StudentList(BaseModel):
    student: list[StudentSchema]

class Student(BaseModel):
    student: StudentSchema


@students_app.get("/students", responses={"200": StudentList})
def get_users():
    with db.session() as session:
        users_query = session.execute(select(Students)).scalars().all()
        users_list = [StudentSchema.from_orm(user).dict() for user in users_query]
        return {"users": users_list}