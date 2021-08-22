from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_faculty, ru_keyboard_faculty, en_keyboard_faculty
from loader import dp, bot


@dp.message_handler(Text(equals="Fakultetlar"))
async def faculty_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institutda 5 ta fakultet mavjud:</b>",
        reply_markup=uz_keyboard_faculty
    )


@dp.message_handler(Text(equals="Факультеты"))
async def faculty_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>В институте 5 факультетов:</b>",
        reply_markup=ru_keyboard_faculty
    )


@dp.message_handler(Text(equals="Faculties"))
async def faculty_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The institute has 5 faculties:</b>",
        reply_markup=en_keyboard_faculty
    )
