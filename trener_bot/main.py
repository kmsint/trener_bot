import logging
from aiogram.utils import executor
from create_bot import dp
import aioschedule, asyncio
from handlers.other import reminder


async def on_startup(_):
    print('Бот вышел в онлайн')
    asyncio.create_task(scheduler())


logging.basicConfig(level=logging.INFO)


async def scheduler():
    aioschedule.every().day.at('8:00').do(reminder)
    aioschedule.every().day.at('15:00').do(reminder)
    aioschedule.every().day.at('20:00').do(reminder)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


from handlers import client, admin, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)