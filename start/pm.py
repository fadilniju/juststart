import logging
from pyrogram import Client, filters, StopPropagation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from mwk_config import Config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.private & filters.command(['start']), group=0)
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Config.START_MSG,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(Config.BUTTON1, url=Config.BUTTONURL1),
                    InlineKeyboardButton(Config.BUTTON2, url=Config.BUTTONURL2)
                ],
                [
                    InlineKeyboardButton(Config.BUTTON3, url=Config.BUTTONURL3)
                ],
            ])
    )
