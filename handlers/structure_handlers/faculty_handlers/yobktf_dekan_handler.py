from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import yobktf_dekani_uz, yobktf_dekani_ru, yobktf_dekani_en

with open("pictures/yobktf_dekan.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Yoqilg‘i va organik birikmalar kimyoviy texnologiyasi fakulteti dekani"))
async def yobktf_dekan_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{yobktf_dekani_uz.get_fullname()}\n\n"
                f"Lavozim    |    {yobktf_dekani_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {yobktf_dekani_uz.get_number()}\n\n"
                f"Email manzil   |   {yobktf_dekani_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {yobktf_dekani_uz.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Декан факультета химической технологии топлив и органических соединений"))
async def yobktf_dekan_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{yobktf_dekani_ru.get_fullname()}\n\n"
                f"Должность    |    {yobktf_dekani_ru.get_position()}\n\n"
                f"Контактный телефон   |   {yobktf_dekani_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {yobktf_dekani_ru.get_email()}\n\n"
                f"Время приема   |   {yobktf_dekani_ru.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Dean of the Faculty of Chemical Technology of Fuels and Organic Compounds"))
async def yobktf_dekan_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{yobktf_dekani_en.get_fullname()}\n\n"
                f"Position    |    {yobktf_dekani_en.get_position()}\n\n"
                f"Contact phone   |   {yobktf_dekani_en.get_number()}\n\n"
                f"Email address   |   {yobktf_dekani_en.get_email()}\n\n"
                f"Reception time   |   {yobktf_dekani_en.get_reception()}\n\n</b>"
    )
