from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import Filial_sh_uz, Filial_sh_ru, Filial_sh_en

with open("pictures/filial_sh.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Shahrisabz filiali direktori"))
async def filial_sh_director_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_sh_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Filial_sh_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Filial_sh_uz.get_number()}\n\n"
                f"Email manzil   |   {Filial_sh_uz.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Директор Шахрисабзского филиала"))
async def filial_sh_director_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_sh_ru.get_fullname()}\n\n"
                f"Должность    |    {Filial_sh_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Filial_sh_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Filial_sh_ru.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Shahrisabz branch director"))
async def filial_sh_director_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Filial_sh_en.get_fullname()}\n\n"
                f"Position    |    {Filial_sh_en.get_position()}\n\n"
                f"Contact phone   |   {Filial_sh_en.get_number()}\n\n"
                f"Email address   |   {Filial_sh_en.get_email()}</b>"
    )
