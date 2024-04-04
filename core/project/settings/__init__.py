from pathlib import Path
import os

#decouple
from decouple import Csv, config
from dotmap import DotMap

ENV = DotMap({'config': config, 'Csv': Csv})
BASE_DIR = Path(__file__).resolve().parent.parent

ADMIN_PATH = ENV.config('ADMIN_PATH')

DEBUG = ENV.config('DEBUG', cast=bool)


from split_settings.tools import optional, include

include(
    'base.py',
    'utils_config.py',
)
if DEBUG:
    include('development.py')
else:
    include('production.py')