import os

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BUTTON1 = os.environ.get("BUTTON1", "")
    BUTTONURL1 = os.environ.get("BUTTONURL1", "")
    BUTTON2 = os.environ.get("BUTTON2", "")
    BUTTONURL2 = os.environ.get("BUTTONURL2", "")
    START_MSG = os.environ.get("START_MSG", "")
    START_IMG = os.environ.get("START_IMG", "")
    OWNERID = set(int(x) for x in os.environ.get("OWNERID", "")
