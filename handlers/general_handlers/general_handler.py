from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_general, ru_keyboard_general, en_keyboard_general
from loader import dp, bot


@dp.message_handler(Text(equals="ℹ Umumiy ma'lumotlar"))
async def general_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Sizga qanday ma'lumot kerak?</b>",
        reply_markup=uz_keyboard_general
    )


@dp.message_handler(Text(equals="ℹ Основная информация"))
async def general_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Какая информация вам нужна?</b>",
        reply_markup=ru_keyboard_general
    )


@dp.message_handler(Text(equals="ℹ General information"))
async def general_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>What information do you need?</b>",
        reply_markup=en_keyboard_general
    )
