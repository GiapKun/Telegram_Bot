import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import TELEGRAM_BOT_TOKEN

class BaseBot:
    def __init__(self, bot_id) -> None:
        self.text_mode = "HTML"
        self.bot = AsyncTeleBot(bot_id)
        self.bot_id = bot_id

    async def send_message(self, message, channel_ids):
        if type(channel_ids) is str:
            channel_ids = [channel_ids]
        for channel_id in channel_ids:
            try:
                await self.bot.send_message(
                    channel_id,
                    message,
                    parse_mode=self.text_mode,
                    disable_web_page_preview=True,
                )
            except Exception as e:
                print(e)

    async def send_sticker(self, sticker_id, channel_ids):
        if type(channel_ids) is str:
            channel_ids = [channel_ids]
        for channel_id in channel_ids:
            try:
                await self.bot.send_sticker(
                    channel_id,
                    sticker_id
                )
            except Exception as e:
                print(e)
            
test_bot = BaseBot(TELEGRAM_BOT_TOKEN)

