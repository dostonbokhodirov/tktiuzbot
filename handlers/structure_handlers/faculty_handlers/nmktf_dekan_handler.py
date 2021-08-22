from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import nmktf_dekani_uz, nmktf_dekani_ru, nmktf_dekani_en

with open("pictures/nmktf_dekan.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Noorganik moddalar kimyoviy texnologiyasi fakulteti dekani"))
async def nmktf_dekan_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{nmktf_dekani_uz.get_fullname()}\n\n"
                f"Lavozim    |    {nmktf_dekani_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {nmktf_dekani_uz.get_number()}\n\n"
                f"Email manzil   |   {nmktf_dekani_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {nmktf_dekani_uz.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Декан факультета химической технологии неорганических веществ"))
async def nmktf_dekan_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{nmktf_dekani_ru.get_fullname()}\n\n"
                f"Должность    |    {nmktf_dekani_ru.get_position()}\n\n"
                f"Контактный телефон   |   {nmktf_dekani_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {nmktf_dekani_ru.get_email()}\n\n"
                f"Время приема   |   {nmktf_dekani_ru.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Dean of the Faculty of Chemical Technology of Inorganic Substances"))
async def nmktf_dekan_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{nmktf_dekani_en.get_fullname()}\n\n"
                f"Position    |    {nmktf_dekani_en.get_position()}\n\n"
                f"Contact phone   |   {nmktf_dekani_en.get_number()}\n\n"
                f"Email address   |   {nmktf_dekani_en.get_email()}\n\n"
                f"Reception time   |   {nmktf_dekani_en.get_reception()}\n\n</b>"
    )
