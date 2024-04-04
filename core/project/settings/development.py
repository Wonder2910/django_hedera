from core.project.settings import BASE_DIR, ENV

SECRET_KEY = ENV.config('SECRET_KEY')


DEBUG = DEBUG  # type: ignore

ALLOWED_HOSTS = ENV.config('ALLOWED_HOSTS', cast=ENV.Csv())