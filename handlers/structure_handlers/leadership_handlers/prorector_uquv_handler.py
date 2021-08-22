from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Prorector_uquv_uz, Prorector_uquv_ru, Prorector_uquv_en

with open("pictures/prorector_uquv.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="O‘quv ishlari bo‘yicha prorektor"))
async def prorector_uquv_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_uquv_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Prorector_uquv_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Prorector_uquv_uz.get_number()}\n\n"
                f"Email manzil   |   {Prorector_uquv_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {Prorector_uquv_uz.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Проректор по учебной работе"))
async def prorector_uquv_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_uquv_ru.get_fullname()}\n\n"
                f"Должность    |    {Prorector_uquv_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Prorector_uquv_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Prorector_uquv_ru.get_email()}\n\n"
                f"Время приема   |   {Prorector_uquv_ru.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Vice Rector for Academic Affairs"))
async def prorector_uquv_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_uquv_en.get_fullname()}\n\n"
                f"Position    |    {Prorector_uquv_en.get_position()}\n\n"
                f"Contact phone   |   {Prorector_uquv_en.get_number()}\n\n"
                f"Email address   |   {Prorector_uquv_en.get_email()}\n\n"
                f"Reception time   |   {Prorector_uquv_en.get_reception()}</b>"
    )
