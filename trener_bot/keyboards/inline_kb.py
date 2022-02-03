from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb_inline = InlineKeyboardMarkup(row_width=3)
inl_btn_1 = InlineKeyboardButton('Ок!', callback_data='ok')
inl_btn_2 = InlineKeyboardButton('Уже!', callback_data='done')

kb_inline.row(inl_btn_1, inl_btn_2)