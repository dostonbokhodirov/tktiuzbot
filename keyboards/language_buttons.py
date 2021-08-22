from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = ["O‘zbek tili 🇺🇿", "Русский 🇷🇺", "English 🇬🇧"]

language_keyboard = InlineKeyboardMarkup(row_width=2)


language_keyboard.add(InlineKeyboardButton(text="O‘zbek tili 🇺🇿", callback_data="UZ"))
language_keyboard.add(InlineKeyboardButton(text="Русский 🇷🇺", callback_data="RU"))
language_keyboard.add(InlineKeyboardButton(text="English 🇬🇧", callback_data="EN"))

# for button in buttons:
#     language_keyboard.insert(InlineKeyboardButton(text=button, callback_data=callback_data_language.new(language=button)))
