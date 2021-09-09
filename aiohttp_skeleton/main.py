import argparse
import logging
import logging.config
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
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    router.setup_routes(app)
    return app


def main():
    logger.info(f'Starting {__package__}')

    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='verbose output',
                        action='store_true', default=False)
    parser.add_argument('-H', '--host', help='hostname or IP to bind on',
                        default=settings.HTTP_HOST)
    parser.add_argument('-P', '--port', help='port to bind on',
                        default=settings.HTTP_PORT)
    params = parser.parse_args()

    application = get_app()
    web.run_app(application, host=params.host, port=params.port)


if __name__ == '__main__':
    main()
