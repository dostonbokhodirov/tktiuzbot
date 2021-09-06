from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=["help"])
async def get_help(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bot yaratuvchisi: @dostonbokhodirov\n"
             f"Taklif va murojaat uchun: @Ernazarov18\n\n"
             f"Создатель бота: @dostonbokhodirov\n"
             f"Для предложений и обращений: @Ernazarov18\n\n"
             f"Bot creator: @dostonbokhodirov\n"
             f"For suggestions and appeals: @Ernazarov18</b>\n\n"
    )
