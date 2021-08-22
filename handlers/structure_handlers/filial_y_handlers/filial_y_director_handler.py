from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import Filial_y_uz, Filial_y_ru, Filial_y_en

with open("pictures/filial_y.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Yangiyer filiali direktori"))
async def filial_y_director_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_y_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Filial_y_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Filial_y_uz.get_number()}\n\n"
                f"Email manzil   |   {Filial_y_uz.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Директор Янгиерского филиала"))
async def filial_y_director_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_y_ru.get_fullname()}\n\n"
                f"Должность    |    {Filial_y_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Filial_y_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Filial_y_ru.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Yangiyer branch director"))
async def filial_y_director_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_y_en.get_fullname()}\n\n"
                f"Position    |    {Filial_y_en.get_position()}\n\n"
                f"Contact phone   |   {Filial_y_en.get_number()}\n\n"
                f"Email address   |   {Filial_y_en.get_email()}</b>"
    )
