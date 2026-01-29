import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5640453720").split()))

API_ID = int(os.getenv("API_ID", "31980058"))

API_HASH = os.getenv("API_HASH", "09e9ba45a244cff03299ad7110b9d968")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7842680732:AAFwqeKZxv5L1cbSpzrKJc2nnR3JNRh2-3k")

OWNER_ID = int(os.getenv("OWNER_ID", "5640453720"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-5236343208").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("mongodb+srv://rahiltobrut_db_user:dapaimup@cluster0.ce7zcpv.mongodb.net/?appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-5236343208"))
