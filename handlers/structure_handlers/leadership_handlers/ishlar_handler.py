from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Ishlar_uz, Ishlar_ru, Ishlar_en

with open("pictures/man.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Ishlar boshqarmasi boshlig‘i"))
async def ishlar_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Ishlar_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Ishlar_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Ishlar_uz.get_number()}\n\n"
                f"Email manzil   |   {Ishlar_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {Ishlar_uz.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Начальник штаба"))
async def ishlar_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Ishlar_ru.get_fullname()}\n\n"
                f"Должность    |    {Ishlar_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Ishlar_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Ishlar_ru.get_email()}\n\n"
                f"Время приема   |   {Ishlar_ru.get_reception()}</b>"
    )


@dp.message_handler(Text(equals="Chief of Staff"))
async def ishlar_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Ishlar_en.get_fullname()}\n\n"
                f"Position    |    {Ishlar_en.get_position()}\n\n"
                f"Contact phone   |   {Ishlar_en.get_number()}\n\n"
                f"Email address   |   {Ishlar_en.get_email()}\n\n"
                f"Reception time   |   {Ishlar_en.get_reception()}</b>"
    )
