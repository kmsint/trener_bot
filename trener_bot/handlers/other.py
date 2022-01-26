from aiogram import types, Dispatcher
from create_bot import dp, bot
from services import *

# @dp.message_handler()
async def echo_send(message : types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    if message.text == 'Тренировка сегодня':
        await bot.send_message(message.from_user.id, 'Сегодня, дружок, тебе предстоит выполнить:')
        await bot.send_message(message.from_user.id, get_training_by_date(get_current_date()))
    elif message.text == 'Следующая':
        await bot.send_message(message.from_user.id, format_training_output(get_next_training()))
    elif message.text == 'Уже выполнено':
        await bot.send_message(message.from_user.id, format_output(get_workouts_done()))
    elif message.text == 'Сколько осталось':
        await bot.send_message(message.from_user.id, format_output(get_workouts_left()))

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo_send)