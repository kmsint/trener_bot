from aiogram import types, Dispatcher
from create_bot import bot
from services import *
from keyboards import kb_inline
from config import USER_ID


async def reminder():
    training_reminder_message = format_training_output(get_training_by_date(get_current_date()))
    # if training_reminder_message != 'Сегодня тренировки нету':
    await bot.send_message(USER_ID, 'Не забудь, дружок, сегодня потренироваться!')
    await bot.send_message(USER_ID, training_reminder_message)
    await bot.send_message(USER_ID, 'Договорились?', reply_markup=kb_inline)

async def ok_call(callback : types.CallbackQuery):
    if callback.data == 'ok':
        await callback.answer('Я напомню тебе позже!', show_alert=True)
    elif callback.data == 'done':
        await callback.message.answer('💪')
    await callback.message.delete()
    await callback.answer()

# @dp.message_handler()
async def main_handler(message : types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    if message.text == 'Тренировка сегодня':
        await bot.send_message(message.from_user.id, 'Сегодня, дружок, тебе предстоит выполнить:')
        await bot.send_message(message.from_user.id, format_training_output(get_training_by_date(get_current_date())))
    elif message.text == 'Следующая':
        await bot.send_message(message.from_user.id, format_training_output(get_next_training()))
    elif message.text == 'Уже выполнено':
        await bot.send_message(message.from_user.id, format_output(get_workouts_done()))
    elif message.text == 'Сколько осталось':
        await bot.send_message(message.from_user.id, format_output(get_workouts_left()))

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(main_handler)
    dp.register_callback_query_handler(ok_call)
