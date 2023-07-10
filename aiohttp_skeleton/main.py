import logging
import os
import sys
from aiohttp import web

from . import db, router


logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))



async def on_startup(app: web.Application):
    await db.init_db(app)


async def on_shutdown(app: web.Application):
    await db.close_db(app)


def get_app():
    app = web.Application(logger=logger)
#    app.on_startup.append(on_startup)
#    app.on_shutdown.append(on_shutdown)
    router.setup_routes(app)
    return app


def main():
    logger.info(f'Starting {__package__}...')
    application = get_app()
    web.run_app(application, host='127.0.0.1', port='8002')


if __name__ == '__main__':
    main()
