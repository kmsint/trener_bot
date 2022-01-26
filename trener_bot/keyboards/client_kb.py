from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_1 = KeyboardButton('Тренировка сегодня')
button_2 = KeyboardButton('Следующая')
button_3 = KeyboardButton('Уже выполнено')
button_4 = KeyboardButton('Сколько осталось')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_client.add(button_1).insert(button_2).add(button_3).insert(button_4)