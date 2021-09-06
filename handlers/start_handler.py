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


@dp.message_handler(user_id=553294971, commands=["users"])
async def stats(message: types.Message):
    users = cursor.execute(f"SELECT username, user_id FROM users").fetchall()
    fullname = cursor.execute(f"SELECT fullname FROM users").fetchall()
    await bot.send_chat_action(message.chat.id, "typing")
    await message.reply(
        text=f"<b>👥 Foydalanuvchilar soni    |    {len(users)} ta:</b>"
                        )
    count = 1
    for user in users:
        if user[0] == "None":
            await bot.send_chat_action(message.chat.id, "typing")
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>{count}.</b> Username mavjud emas!\n"
                     f"Foydalanuvchining ID raqami: <code>{user[1]}</code>"
            )
            count += 1
        else:
            await bot.send_chat_action(message.chat.id, "typing")
            await bot.send_message(
                chat_id=message.chat.id,
                text=f"<b>{count}.</b> @{user[0]}"
            )
            count += 1
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>{fullname}</b>"
    )
