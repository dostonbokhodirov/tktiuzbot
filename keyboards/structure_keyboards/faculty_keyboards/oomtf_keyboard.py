from aiogram import types

uz_keyboard_oomtf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_oomtf.add("Oziq-ovqat mahsulotlari texnologiyasi fakulteti dekani")
uz_keyboard_oomtf.add("Oziq-ovqat mahsulotlari texnologiyasi fakulteti kafedralari")
uz_keyboard_oomtf.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_oomtf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_oomtf.add("Декан факультета пищевых технологий")
ru_keyboard_oomtf.add("Кафедры факультета пищевых технологий")
ru_keyboard_oomtf.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_oomtf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_oomtf.add("Dean of the Faculty of Food Technology")
en_keyboard_oomtf.add("Departments of the Faculty of Food Technology")
en_keyboard_oomtf.row("🔙 Back", "🔝 Main menu")
