import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

if bool(os.environ.get("WEBHOOK", False)):
    from mwk_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    plugins = dict(
        root="start"
    )
    app = pyrogram.Client(
        "Start Bot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=start
    )
    Config.AUTH_USERS.add(749673781)
    app.run()
