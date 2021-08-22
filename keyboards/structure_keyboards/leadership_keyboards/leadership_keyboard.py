from aiogram import types

uz_keyboard_leadership = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
uz_keyboard_leadership.add("Rektor")
uz_keyboard_leadership.add("O‘quv ishlari bo‘yicha prorektor")
uz_keyboard_leadership.add("Ilmiy ishlar va innovatsiyalar bo‘yicha prorektor")
uz_keyboard_leadership.add("Yoshlar bilan ishlash bo‘yicha prorektor")
uz_keyboard_leadership.add("Ishlar boshqarmasi boshlig‘i")
uz_keyboard_leadership.row("🔙 Orqaga", "🔝 Bosh menyu")

ru_keyboard_leadership = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
ru_keyboard_leadership.add("Ректор")
ru_keyboard_leadership.add("Проректор по учебной работе")
ru_keyboard_leadership.add("Проректор по исследованиям и инновациям")
ru_keyboard_leadership.add("Проректор по делам молодежи")
ru_keyboard_leadership.add("Начальник штаба")
ru_keyboard_leadership.row("🔙 Назад", "🔝 Главное меню")

en_keyboard_leadership = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True, resize_keyboard=True)
en_keyboard_leadership.add("Rector")
en_keyboard_leadership.add("Vice Rector for Academic Affairs")
en_keyboard_leadership.add("Vice Rector for Research and Innovation")
en_keyboard_leadership.add("Vice Rector for Youth Affairs")
en_keyboard_leadership.add("Chief of Staff")
en_keyboard_leadership.row("🔙 Back", "🔝 Main menu")
