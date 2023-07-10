from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey,
                        Index, Integer, Numeric, Unicode, UnicodeText, )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils.types import ChoiceType

from . import db


class User(db.Base):
    __tablename__ = 'auth_user'

    id = Column(Integer, primary_key=True)
    username = Column(Unicode(256))
    first_name = Column(Unicode(256))
    last_name = Column(Unicode(256))
    is_staff = Column(Boolean)

    def get_id(self):
        return User.query.filter_by(id=2).one()
