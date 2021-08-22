from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import vtsuf_dekani_uz, vtsuf_dekani_ru, vtsuf_dekani_en

with open("pictures/vtsuf_dekan.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Vinochilik texnologiyasi va sanoat uzumchiligi fakulteti dekani"))
async def vtsuf_dekan_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{vtsuf_dekani_uz.get_fullname()}\n\n"
                f"Lavozim    |    {vtsuf_dekani_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {vtsuf_dekani_uz.get_number()}\n\n"
                f"Email manzil   |   {vtsuf_dekani_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {vtsuf_dekani_uz.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Декан факультета технологии вина и промышленного виноградарства"))
async def vtsuf_dekan_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{vtsuf_dekani_ru.get_fullname()}\n\n"
                f"Должность    |    {vtsuf_dekani_ru.get_position()}\n\n"
                f"Контактный телефон   |   {vtsuf_dekani_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {vtsuf_dekani_ru.get_email()}\n\n"
                f"Время приема   |   {vtsuf_dekani_ru.get_reception()}\n\n</b>"
    )


@dp.message_handler(Text(equals="Dean of the Faculty of Wine Technology and Industrial Viticulture"))
async def vtsuf_dekan_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{vtsuf_dekani_en.get_fullname()}\n\n"
                f"Position    |    {vtsuf_dekani_en.get_position()}\n\n"
                f"Contact phone   |   {vtsuf_dekani_en.get_number()}\n\n"
                f"Email address   |   {vtsuf_dekani_en.get_email()}\n\n"
                f"Reception time   |   {vtsuf_dekani_en.get_reception()}\n\n</b>"
    )
