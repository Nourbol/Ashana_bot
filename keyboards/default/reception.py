from aiogram.types  import ReplyKeyboardMarkup, KeyboardButton


reception = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu ๐'),
        ],
        [
            KeyboardButton(text='My orders ๐งพ'),
        ],
        [
            KeyboardButton(text='Cart ๐'),
        ],
    ],
    resize_keyboard=True
)