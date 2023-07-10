import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

Base = declarative_base()


async def init_db(app):
    from . import models
    sa_engine = create_engine('mysql://ccc_is:ccc_is@127.0.0.1/ccc_is')
    db_session = scoped_session(sessionmaker(bind=sa_engine, autocommit=False, autoflush=False))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=sa_engine)
    app.db_engine = sa_engine
    app.db_session = db_session


async def close_db(app):
    app.db_session.remove()
    app.db_engine.dispose()
