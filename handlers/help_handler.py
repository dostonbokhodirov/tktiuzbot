from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=["help"])
async def get_help(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"✍ <b>Taklif va murojaatlaringizni <a href='https://t.me/Ernazarov18'>Davronga</a> yoki <a href='https://t.me/dostonbokhodirov'>Dostonga</a> yozishingiz mumkin.\n\n"
             f"✍ Вы можете писать свои предложения и обращения <a href='https://t.me/Ernazarov18'>Даврону</a> или <a href='https://t.me/dostonbokhodirov'>Достону</a>.\n\n"
             f"✍ You can write your suggestions and appeals to <a href='https://t.me/Ernazarov18'>Davron</a> or to <a href='https://t.me/dostonbokhodirov'>Doston</a>.</b>"
    )
