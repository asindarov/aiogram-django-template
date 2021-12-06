from django_settings import *
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram import types
from config import I18N_DOMAIN, LOCALES_DIR
from asgiref.sync import sync_to_async
from db.models import User

async def get_lang(user_id):
    print(user_id)
    try:
        user = User.objects.get(id=user_id)
    except:
        user = None    
    # print(user.language)
    if user:
        return user.language


class ACLMiddleware(I18nMiddleware):
    async def get_user_locale(self, action, args):
        user = types.User.get_current()
        return await get_lang(user.id) or user.locale


def setup_middleware(dp):
    i18n = ACLMiddleware(I18N_DOMAIN, LOCALES_DIR)
    dp.middleware.setup(i18n)
    return i18n