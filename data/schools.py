import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class School(SqlAlchemyBase):
    __tablename__ = 'schools'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    users = orm.relationship("User", back_populates='school')
    students = orm.relationship("Student", back_populates='school')