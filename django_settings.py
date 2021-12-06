import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
import django
django.setup()
from asgiref.sync import sync_to_async
from db.models import *
