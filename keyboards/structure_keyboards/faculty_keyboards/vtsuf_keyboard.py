from aiogram import types

uz_keyboard_vtsuf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_vtsuf.add("Vinochilik texnologiyasi va sanoat uzumchiligi fakulteti dekani")
uz_keyboard_vtsuf.add("Vinochilik texnologiyasi va sanoat uzumchiligi fakulteti kafedralari")
uz_keyboard_vtsuf.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_vtsuf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_vtsuf.add("Декан факультета технологии вина и промышленного виноградарства")
ru_keyboard_vtsuf.add("Кафедры факультета технологии вина и промышленного виноградарства")
ru_keyboard_vtsuf.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_vtsuf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_vtsuf.add("Dean of the Faculty of Wine Technology and Industrial Viticulture")
en_keyboard_vtsuf.add("Departments of the Faculty of Wine Technology and Industrial Viticulture")
en_keyboard_vtsuf.row("🔙 Back", "🔝 Main menu")
