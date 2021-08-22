from aiogram import types

uz_keyboard_general = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_general.add("📋 Institut haqida")
uz_keyboard_general.row("🗺 Institut manzili", "☎ Institut bilan aloqa")
uz_keyboard_general.add("🔝 Bosh menyu")

ru_keyboard_general = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_general.add("📋 Об институте")
ru_keyboard_general.row("🗺 Адрес института", "☎ Связь с институтом")
ru_keyboard_general.add("🔝 Главное меню")

en_keyboard_general = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_general.add("📋 About the institute")
en_keyboard_general.row("🗺 Institute address", "☎ Contact with the institute")
en_keyboard_general.add("🔝 Main menu")