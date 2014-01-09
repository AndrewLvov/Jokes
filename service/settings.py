DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306, # MySQL default port
    'user': '',
    'passwd': '',
    'db': '',
}

try:
    from local_settings import *
except ImportError:
    pass