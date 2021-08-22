from aiogram import types

uz_keyboard_mktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_mktf.add("Menejment va kasb ta'limi fakulteti dekani")
uz_keyboard_mktf.add("Menejment va kasb ta'limi fakulteti kafedralari")
uz_keyboard_mktf.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_mktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_mktf.add("Декан факультета менеджмента и профессионального образования")
ru_keyboard_mktf.add("Кафедры факультета менеджмента и профессионального образования")
ru_keyboard_mktf.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_mktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_mktf.add("Dean of the Faculty of Management and Vocational Education")
en_keyboard_mktf.add("Departments of the Faculty of Management and Vocational Education")
en_keyboard_mktf.row("🔙 Back", "🔝 Main menu")
