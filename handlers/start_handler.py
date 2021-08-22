from aiogram import types

from loader import dp, bot, cursor, connect
from keyboards import language_keyboard


@dp.message_handler(commands=["start", "language"])
async def welcome(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"🇺🇿 Iltimos, tilni tanlang: \n"
             f"🇷🇺 Пожалуйста, выберите язык: \n"
             f"🇬🇧 Please select a language: ",
        reply_markup=language_keyboard
    )
    info = [message.from_user.id, message.from_user.full_name, message.from_user.username, message.from_user.language_code]
    cursor.execute(f"INSERT INTO users VALUES(?, ?, ?, ?);", info)
    connect.commit()


@dp.message_handler(commands=["users"])
async def stats(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    users_fullnames = cursor.execute(f"SELECT fullname FROM users").fetchall()
    users_usernames = cursor.execute(f"SELECT username  FROM users").fetchall()
    await message.answer(f"<b>👥 Foydalanuvchilar soni    |    {len(users_fullnames)} ta</b>\n"
                         f"{users_fullnames}\n\n"
                         f"{users_usernames}")
