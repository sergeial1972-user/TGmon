#imports
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


main_menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📊 Status")],
        [KeyboardButton(text="⚙️ Settings")],
        [KeyboardButton(text="🔙 Go back")],
    ]
)