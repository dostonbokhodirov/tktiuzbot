from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_address, ru_keyboard_address, en_keyboard_address
from loader import dp, bot


@dp.message_handler(Text(equals="🗺 Institut manzili"))
async def address_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institut bosh binosini yoki kerakli fakultet binosini tanlang:</b>",
        reply_markup=uz_keyboard_address
    )


@dp.message_handler(Text(equals="🗺 Адрес института"))
async def address_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Выберите главный корпус института или желаемый корпус факультета:</b>",
        reply_markup=ru_keyboard_address
    )


@dp.message_handler(Text(equals="🗺 Institute address"))
async def address_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Select the main building of the institute or the desired faculty building:</b>",
        reply_markup=en_keyboard_address
    )
