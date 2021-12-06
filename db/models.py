import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=250, blank=True)
    username = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250, blank=True)
    language = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"ism : {self.name} tel : {self.phone} til : {self.language}"

