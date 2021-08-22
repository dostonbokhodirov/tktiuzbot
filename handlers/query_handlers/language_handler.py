import asyncio

from keyboards import uz_keyboard, ru_keyboard, en_keyboard
from loader import dp, bot
from aiogram import types


@dp.callback_query_handler(lambda c: c.data == 'UZ')
async def uzbek(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id, text=f"Assalomu alaykum, <b>{callback_query.from_user.full_name}</b>")
    await asyncio.sleep(1)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"<b>Toshkent kimyo-texnologiya institutining rasmiy botiga xush kelibsiz!</b>",
        reply_markup=uz_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'RU')
async def russian(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id, text=f"Здравствуйте, <b>{callback_query.from_user.full_name}</b>")
    await asyncio.sleep(1)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"<b>Добро пожаловать в официальный бот Ташкентского химико-технологического института!</b>",
        reply_markup=ru_keyboard
    )


@dp.callback_query_handler(lambda c: c.data == 'EN')
async def english(callback_query: types.CallbackQuery):
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        chat_id=callback_query.from_user.id, text=f"Hello, <b>{callback_query.from_user.full_name}</b>")
    await asyncio.sleep(1)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"<b>Welcome to the official bot of the Tashkent Chemical-Technological Institute!</b>",
        reply_markup=en_keyboard
    )
