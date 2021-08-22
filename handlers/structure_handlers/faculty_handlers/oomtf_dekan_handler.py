from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import oomtf_dekani_uz, oomtf_dekani_ru, oomtf_dekani_en

with open("pictures/oomtf_dekan.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Oziq-ovqat mahsulotlari texnologiyasi fakulteti dekani"))
async def oomtf_dekan_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{oomtf_dekani_uz.get_fullname()}\n\n"
                f"Lavozim    |    {oomtf_dekani_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {oomtf_dekani_uz.get_number()}\n\n"
                f"Email manzil   |   {oomtf_dekani_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {oomtf_dekani_uz.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Декан факультета пищевых технологий"))
async def oomtf_dekan_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{oomtf_dekani_ru.get_fullname()}\n\n"
                f"Должность    |    {oomtf_dekani_ru.get_position()}\n\n"
                f"Контактный телефон   |   {oomtf_dekani_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {oomtf_dekani_ru.get_email()}\n\n"
                f"Время приема   |   {oomtf_dekani_ru.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Dean of the Faculty of Food Technology"))
async def oomtf_dekan_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{oomtf_dekani_en.get_fullname()}\n\n"
                f"Position    |    {oomtf_dekani_en.get_position()}\n\n"
                f"Contact phone   |   {oomtf_dekani_en.get_number()}\n\n"
                f"Email address   |   {oomtf_dekani_en.get_email()}\n\n"
                f"Reception time   |   {oomtf_dekani_en.get_reception()}\n\n</b>"
    )
