from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import mktf_dekani_uz, mktf_dekani_ru, mktf_dekani_en

with open("pictures/mktf_dekan.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Menejment va kasb ta'limi fakulteti dekani"))
async def mktf_dekan_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{mktf_dekani_uz.get_fullname()}\n\n"
                f"Lavozim    |    {mktf_dekani_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {mktf_dekani_uz.get_number()}\n\n"
                f"Email manzil   |   {mktf_dekani_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {mktf_dekani_uz.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Декан факультета менеджмента и профессионального образования"))
async def mktf_dekan_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{mktf_dekani_ru.get_fullname()}\n\n"
                f"Должность    |    {mktf_dekani_ru.get_position()}\n\n"
                f"Контактный телефон   |   {mktf_dekani_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {mktf_dekani_ru.get_email()}\n\n"
                f"Время приема   |   {mktf_dekani_ru.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Dean of the Faculty of Management and Vocational Education"))
async def mktf_dekan_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{mktf_dekani_en.get_fullname()}\n\n"
                f"Position    |    {mktf_dekani_en.get_position()}\n\n"
                f"Contact phone   |   {mktf_dekani_en.get_number()}\n\n"
                f"Email address   |   {mktf_dekani_en.get_email()}\n\n"
                f"Reception time   |   {mktf_dekani_en.get_reception()}\n\n</b>"
    )
