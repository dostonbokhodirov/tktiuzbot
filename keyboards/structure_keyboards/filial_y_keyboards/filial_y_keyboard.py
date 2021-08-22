from aiogram import types

uz_keyboard_filial_y = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_filial_y.add("Yangiyer filiali direktori")
uz_keyboard_filial_y.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_filial_y = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_filial_y.add("Директор Янгиерского филиала")
ru_keyboard_filial_y.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_filial_y = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_filial_y.add("Yangiyer branch director")
en_keyboard_filial_y.row("🔙 Back", "🔝 Main menu")
