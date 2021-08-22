from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_social, ru_keyboard_social, en_keyboard_social, keyboard_social_2
from loader import dp, bot


@dp.message_handler(Text(equals="🌐 Institut ijtimoiy tarmoqlarda"))
async def social_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institutning rasmiy sahifalari:</b>",
        reply_markup=uz_keyboard_social
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institut matbuot xizmatining rasmiy sahifalari:</b>",
        reply_markup=keyboard_social_2
    )


@dp.message_handler(Text(equals="🌐 Институт в социальных сетях"))
async def social_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Официальные страницы института:</b>",
        reply_markup=ru_keyboard_social
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Официальные страницы пресс-службы института:</b>",
        reply_markup=keyboard_social_2
    )


@dp.message_handler(Text(equals="🌐 The institute is on social networks"))
async def social_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Official pages of the institute:</b>",
        reply_markup=en_keyboard_social
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Official pages of the press service of the institute:</b>",
        reply_markup=keyboard_social_2
    )
