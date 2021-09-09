import os


def get_env_var(var_name, var_default):
    try:
        return os.environ[var_name]
    except KeyError:
        return var_default


HTTP_HOST = get_env_var('HTTP_HOST', '127.0.0.1')
HTTP_PORT = get_env_var('HTTP_PORT', 8000)

DATABASE_URL = get_env_var(
    'DATABASE_URL', 'sql://user@password@localhost:12345/database'
)

LOGGING_FILENAME = 'logs/app.log'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LOGGING_FILENAME,
            'maxBytes': 10 * 1024 * 1024,
            'backupCount': 1,
        }
    },
    'loggers': {
        'asyncio': {
            'level': 'WARNING',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
        'aiohttp': {
            'level': 'WARNING',
            'handlers': ['console', 'file'],
            'propagate': False,
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    },
}
