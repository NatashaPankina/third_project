import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Student(SqlAlchemyBase):
    __tablename__ = 'students'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    class_writing = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    class_take = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    school_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("schools.id"), nullable=False)
    school = orm.relationship('School')
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    olymp_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("olympiads.id"), nullable=False)
    olympiad = orm.relationship('Olympiad')
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=False)
    user = orm.relationship('User')
    year = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    