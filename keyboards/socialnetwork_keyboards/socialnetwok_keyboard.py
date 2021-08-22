from aiogram import types

uz_keyboard_social = types.InlineKeyboardMarkup(row_width=3)
uz_keyboard_social.add(types.InlineKeyboardButton(text="Institut rasmiy sayti", url="http://tkti.uz"))
uz_keyboard_social.add(types.InlineKeyboardButton(text="Yoshlar Ittifoqi telegram kanali", url="https://t.me/TKTI_Official"))
uz_keyboard_social.add(types.InlineKeyboardButton(text="Xalqaro hamkorlik telegram kanali", url="https://t.me/tkti_international"))

ru_keyboard_social = types.InlineKeyboardMarkup(row_width=3)
ru_keyboard_social.add(types.InlineKeyboardButton(text="Официальный сайт института", url="http://tkti.uz/ru"))
ru_keyboard_social.add(types.InlineKeyboardButton(text="Телеграм канал Союза Молодежи", url="https://t.me/TKTI_Official"))
ru_keyboard_social.add(types.InlineKeyboardButton(text="Телеграм канал международного сотрудничества", url="https://t.me/tkti_international"))

en_keyboard_social = types.InlineKeyboardMarkup(row_width=3)
en_keyboard_social.add(types.InlineKeyboardButton(text="Official site", url="http://tkti.uz/en"))
en_keyboard_social.add(types.InlineKeyboardButton(text="Youth Union Telegram Channel", url="https://t.me/TKTI_Official"))
en_keyboard_social.add(types.InlineKeyboardButton(text="International Cooperation Telegram Channel", url="https://t.me/tkti_international"))

keyboard_social_2 = types.InlineKeyboardMarkup(row_width=3)
keyboard_social_2.add(types.InlineKeyboardButton(text="Telegram", url="https://t.me/tktimatbuotxizmati"))
keyboard_social_2.add(types.InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/tkti.matbuotxizmati"))
keyboard_social_2.add(types.InlineKeyboardButton(text="Youtube", url="https://youtube.com/channel/UCMBthWkBnRKxzhrbizwXc4g"))
