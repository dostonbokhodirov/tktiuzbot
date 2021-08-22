from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_structure, ru_keyboard_structure, en_keyboard_structure
from loader import dp, bot


@dp.message_handler(Text(equals="🏫 Tuzilma"))
async def structure_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Kerakli institut tuzilmasini tanlang:</b>",
        reply_markup=uz_keyboard_structure
    )


@dp.message_handler(Text(equals="🏫 Структура"))
async def structure_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Выберите желаемую структуру заведения:</b>",
        reply_markup=ru_keyboard_structure
    )


@dp.message_handler(Text(equals="🏫 Structure"))
async def structure_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Select the desired institution structure:</b>",
        reply_markup=en_keyboard_structure
    )
