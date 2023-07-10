import logging

from aiohttp import web

from . import db, models


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


async def index(request):
    sess = request.app.db_session
    user = models.User.query.filter_by(username='root').one()
    return web.json_response({
        'username': user.username,
        'user_id': user.get_id().username,
    })
