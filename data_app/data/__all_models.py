import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Form(SqlAlchemyBase):
    __tablename__ = "forms"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    form_uid = sqlalchemy.Column(sqlalchemy.String, unique=True)
    creation_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())

    elements = orm.relation("Element", back_populates="form")
    values = orm.relation("FormValues", back_populates="form")


class Element(SqlAlchemyBase):
    __tablename__ = "elements"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    form_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("forms.id"))
    form = orm.relation("Form")

    type = sqlalchemy.Column(sqlalchemy.String)
    placeholder = sqlalchemy.Column(sqlalchemy.String)
    is_required = sqlalchemy.Column(sqlalchemy.Boolean, default=False)


class FormValues(SqlAlchemyBase):
    __tablename__ = "values"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    form_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("forms.id"))
    form = orm.relation("Form")

    values = sqlalchemy.Column(sqlalchemy.String)
