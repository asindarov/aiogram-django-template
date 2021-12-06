from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
admin_id = os.environ.get("admin_id")
BASE_DIR = Path(__file__).parent
I18N_DOMAIN = os.environ.get("I18N_DOMAIN")
LOCALES_DIR = BASE_DIR/"locales"
ESKIZ_TOKEN = os.environ.get("ESKIZ_TOKEN")
