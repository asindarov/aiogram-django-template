
import sys
sys.dont_write_bytecode = True

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from db.models import *

# User.objects.create(name='Dan')
# User.objects.create(name='Robert')

# for u in User.objects.all():
#     print(f'ID: {u.id} \tUsername: {u.name}')
