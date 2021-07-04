import os

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BUTTON1 = os.environ.get("BUTTON1_URL", "")
    BUTTON2 = os.environ.get("BUTTON2_URL", "")
    START_MSG = os.environ.get("START_MSG", "")
    OWNERID = set(int(x) for x in os.environ.get("OWNERID", "").split())
