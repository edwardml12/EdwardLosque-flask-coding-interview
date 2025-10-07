from sqlalchemy.orm import Mapped, mapped_column

from api.db import Base


class Students(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(nullable=False)
    enrollment_date: Mapped[str] = mapped_column(nullable=False)
    updated_at: Mapped[str] = mapped_column(nullable=False)
    min_course_credits: Mapped[str] = mapped_column(nullable=True)
