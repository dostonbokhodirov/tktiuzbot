from aiogram import types

uz_keyboard_nmktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_nmktf.add("Noorganik moddalar kimyoviy texnologiyasi fakulteti dekani")
uz_keyboard_nmktf.add("Noorganik moddalar kimyoviy texnologiyasi fakulteti kafedralari")
uz_keyboard_nmktf.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_nmktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_nmktf.add("Декан факультета химической технологии неорганических веществ")
ru_keyboard_nmktf.add("Кафедры факультета химической технологии неорганических веществ")
ru_keyboard_nmktf.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_nmktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_nmktf.add("Dean of the Faculty of Chemical Technology of Inorganic Substances")
en_keyboard_nmktf.add("Departments of the Faculty of Chemical Technology of Inorganic Substances")
en_keyboard_nmktf.row("🔙 Back", "🔝 Main menu")
