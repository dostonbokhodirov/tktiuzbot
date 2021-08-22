from aiogram import types


uz_keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard.add("ℹ Umumiy ma'lumotlar")
uz_keyboard.add("🏫 Tuzilma")
uz_keyboard.add("🌐 Institut ijtimoiy tarmoqlarda")


ru_keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard.add("ℹ Основная информация")
ru_keyboard.add("🏫 Структура")
ru_keyboard.add("🌐 Институт в социальных сетях")

en_keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard.add("ℹ General information")
en_keyboard.add("🏫 Structure")
en_keyboard.add("🌐 The institute is on social networks")
