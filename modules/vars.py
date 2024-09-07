import os

API_ID    = os.environ.get("API_ID", "21827228")
API_HASH  = os.environ.get("API_HASH", "306c60a42c7b0d6b706c91beab097483")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6991697056:AAGwBuc9l1hY4l_YFVHBLd60nMMca3kuBoA") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
