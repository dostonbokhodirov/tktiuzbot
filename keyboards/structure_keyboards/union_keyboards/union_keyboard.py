from aiogram import types

uz_keyboard_union = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_union.add("Yoshlar Ittifoqi yetakchisi")
uz_keyboard_union.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_union = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_union.add("Лидер Союза молодежи")
ru_keyboard_union.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_union = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_union.add("Leader of the Youth Union")
en_keyboard_union.row("🔙 Back", "🔝 Main menu")
