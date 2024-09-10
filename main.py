import asyncio
from bot import test_bot
from config import CHANNEL_ID

async def main():
    result = await test_bot.send_sticker("CAACAgUAAx0CeBdZkgACAblmyEn-jpLYNQABbakhCGJKAqkFMvgAAngEAAKlqvlXjptEjbU3an81BA", CHANNEL_ID)

# Khởi động vòng lặp sự kiện để chạy hàm bất đồng bộ
if __name__ == "__main__":
    asyncio.run(main())
