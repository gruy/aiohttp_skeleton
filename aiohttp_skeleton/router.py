import logging
from aiohttp import web

from . import views


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def setup_routes(app):
    app.router.add_get('/', views.index)
