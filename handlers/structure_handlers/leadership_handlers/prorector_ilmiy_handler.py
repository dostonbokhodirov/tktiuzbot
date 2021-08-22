from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Prorector_ilmiy_uz, Prorector_ilmiy_ru, Prorector_ilmiy_en

with open("pictures/prorector_ilmiy.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Ilmiy ishlar va innovatsiyalar bo‘yicha prorektor"))
async def prorector_ilmiy_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_ilmiy_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Prorector_ilmiy_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Prorector_ilmiy_uz.get_number()}\n\n"
                f"Email manzil   |   {Prorector_ilmiy_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {Prorector_ilmiy_uz.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Проректор по исследованиям и инновациям"))
async def prorector_ilmiy_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_ilmiy_ru.get_fullname()}\n\n"
                f"Должность    |    {Prorector_ilmiy_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Prorector_ilmiy_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Prorector_ilmiy_ru.get_email()}\n\n"
                f"Время приема   |   {Prorector_ilmiy_ru.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Vice Rector for Research and Innovation"))
async def prorector_ilmiy_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Prorector_ilmiy_en.get_fullname()}\n\n"
                f"Position    |    {Prorector_ilmiy_en.get_position()}\n\n"
                f"Contact phone   |   {Prorector_ilmiy_en.get_number()}\n\n"
                f"Email address   |   {Prorector_ilmiy_en.get_email()}\n\n"
                f"Reception time   |   {Prorector_ilmiy_en.get_reception()}</b>"
    )
