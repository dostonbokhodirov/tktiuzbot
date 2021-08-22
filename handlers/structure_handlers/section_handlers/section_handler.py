from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_section, ru_keyboard_section, en_keyboard_section
from loader import dp, bot


@dp.message_handler(Text(equals="Bo‘limlar va markazlar"))
async def section_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institutda quyidagi bo‘limlar va markazlar faoliyat yuritmoqda:</b>",
        reply_markup=uz_keyboard_section
    )


@dp.message_handler(Text(equals="Отделения и центры"))
async def section_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>В институте действуют следующие отделения и центры:</b>",
        reply_markup=ru_keyboard_section
    )


@dp.message_handler(Text(equals="Departments and centres"))
async def section_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The institute has the following departments and centres:</b>",
        reply_markup=en_keyboard_section
    )
