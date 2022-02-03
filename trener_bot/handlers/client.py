from aiogram import Dispatcher, types
from create_bot import bot
from keyboards import kb_client
from services import get_current_date, get_training_by_date

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    print(message.text)
    await bot.send_message(message.from_user.id, 'Потренеруемся!', reply_markup=kb_client)
    # await bot.send_message(message.from_user.id, 'Для бота доступны следующие команды:')
    # await bot.send_message(message.from_user.id, '1. Тренировка сегодня\n2. Следующая тренировка\n3. Уже выполнено\n4. Сколько осталось')
    # await bot.send_message(message.from_user.id, reply_markup=kb_client)


# @dp.message_handler(commands=['Тренировка сегодня'])
async def command_today_training(message : types.Message):
    print(message.text)
    # if message.text == 'Тренировка_сегодня':
    await bot.send_message(message.from_user.id, 'Сегодня, дружок, тебе предстоит выполнить:')
    await bot.send_message(message.from_user.id, get_training_by_date(get_current_date()))


# @dp.message_handler(commands=['Следующая тренировка'])
async def command_next_traning(message : types.Message):
    await bot.send_message(message.from_user.id, 'Потренеруемся!')


# @dp.message_handler(commands=['Уже выполнено'])
async def command_done(message : types.Message):
    await bot.send_message(message.from_user.id, 'Потренеруемся!')


# @dp.message_handler(commands=['Сколько осталось'])
async def command_to_do(message : types.Message):
    await bot.send_message(message.from_user.id, 'Потренеруемся!')


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(command_today_training, commands=['Тренировка сегодня'])
    dp.register_message_handler(command_next_traning, commands=['Следующая'])
    dp.register_message_handler(command_done, commands=['Уже выполнено'])
    dp.register_message_handler(command_to_do, commands=['Сколько осталось'])
