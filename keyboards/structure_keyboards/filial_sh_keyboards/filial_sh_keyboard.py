from aiogram import types

uz_keyboard_filial_sh = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_filial_sh.add("Shahrisabz filiali direktori")
uz_keyboard_filial_sh.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_filial_sh = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_filial_sh.add("Директор Шахрисабзского филиала")
ru_keyboard_filial_sh.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_filial_sh = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_filial_sh.add("Shahrisabz branch director")
en_keyboard_filial_sh.row("🔙 Back", "🔝 Main menu")
