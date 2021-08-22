from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_leadership, ru_keyboard_leadership, en_keyboard_leadership
from loader import dp, bot


@dp.message_handler(Text(equals="Institut rahbariyati"))
async def leadership_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institut rahbariyati:</b>",
        reply_markup=uz_keyboard_leadership
    )


@dp.message_handler(Text(equals="Руководство института"))
async def leadership_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Руководство института:</b>",
        reply_markup=ru_keyboard_leadership
    )


@dp.message_handler(Text(equals="Institute leadership"))
async def leadership_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institute leadership:</b>",
        reply_markup=en_keyboard_leadership
    )
