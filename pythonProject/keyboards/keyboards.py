from aiogram import types


button1 = types.KeyboardButton(text='Старт')
button2 = types.KeyboardButton(text='Выбор профессии')
button3 = types.KeyboardButton(text='Сыграем?')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='Стоп')


keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]

keyboard2 = [
    [button1, button5],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
