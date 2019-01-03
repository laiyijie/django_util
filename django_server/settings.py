LOGGING_LEVEL = os.environ.get("LOGGING_LEVEL", "INFO")
ENV = os.getenv("ENV", "DEFAULT")
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'utils.exception_middleware.ExceptionReportMiddleware',
    'utils.request_parse_middleware.RequestBodyMiddleware',
    'utils.users_auth_middleware.UsersAuthMiddleWare',
]
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(filename)s %(lineno)d %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'access': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'filename': '/var/log/dec_server/dec.log',
            'formatter': 'verbose',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',  # this specifies the interval
            'interval': 7,  # defaults to 1, only necessary for other values
            'backupCount': 10,  # how many backup file to keep, 10 days
        },
        'console': {
            'level': LOGGING_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
        'access_file': {
            'filename': '/var/log/dec_server/access.log',
            'formatter': 'access',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 'D',  # this specifies the interval
            'interval': 7,  # defaults to 1, only necessary for other values
            'backupCount': 10,  # how many backup file to keep, 10 days
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': LOGGING_LEVEL,
            'propagate': True,
        },
        'access': {
            'handlers': ['access_file', ],
            'level': LOGGING_LEVEL,
            'propagate': False,
        }
    },
}

if os.environ.get("CONSOLE_LOG_ONLY"):
    LOGGING["handlers"]["access_file"] = LOGGING["handlers"]["console"]
    LOGGING["handlers"]["file"] = LOGGING["handlers"]["console"]
DEFAULT_DB_HOST = os.getenv('DEFAULT_DB_HOST')
DEFAULT_DB_PORT = os.getenv('DEFAULT_DB_PORT')
DEFAULT_DB_USERNAME = os.getenv('DEFAULT_DB_USERNAME')
DEFAULT_DB_PASSWORD = os.getenv('DEFAULT_DB_PASSWORD')
DEFAULT_DB_NAME = os.getenv('DEFAULT_DB_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': DEFAULT_DB_HOST,
        'PORT': DEFAULT_DB_PORT,
        'NAME': DEFAULT_DB_NAME,
        'USER': DEFAULT_DB_USERNAME,
        'PASSWORD': DEFAULT_DB_PASSWORD,
        'CONN_MAX_AGE': 3000,
        'RECYCLE_TIME': 3000,
    }
}

if ENV == "LOCAL":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

