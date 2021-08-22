from aiogram import types

uz_keyboard_yobktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_yobktf.add("Yoqilg‘i va organik birikmalar kimyoviy texnologiyasi fakulteti dekani")
uz_keyboard_yobktf.add("Yoqilg‘i va organik birikmalar kimyoviy texnologiyasi fakulteti kafedralari")
uz_keyboard_yobktf.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_yobktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_yobktf.add("Декан факультета химической технологии топлив и органических соединений")
ru_keyboard_yobktf.add("Кафедры химической технологии топлив и органических соединений")
ru_keyboard_yobktf.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_yobktf = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_yobktf.add("Dean of the Faculty of Chemical Technology of Fuels and Organic Compounds")
en_keyboard_yobktf.add("Departments of the Faculty of Chemical Technology of Fuels and Organic Compounds")
en_keyboard_yobktf.row("🔙 Back", "🔝 Main menu")
