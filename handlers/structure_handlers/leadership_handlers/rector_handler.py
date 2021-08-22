from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import Rector_uz, Rector_ru, Rector_en

with open("pictures/rector.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Rektor"))
async def rector_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Rector_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Rector_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Rector_uz.get_number()}\n\n"
                f"Email manzil   |   {Rector_uz.get_email()}\n\n"
                f"Qabul vaqti   |   {Rector_uz.get_reception()}\n\n"
                f"Rasmiy ijtimoiy tarmoq sahifalari:\n\n"
                f"<a href='https://t.me/tkti_rektor'>Telegram</a>    |    <a href='https://www.facebook.com/botir.usmonov.5'>Facebook</a>    |    <a href='https://twitter.com/botir2468'>Twitter</a>\n\n"
                f"<a href='https://telegra.ph/Toshkent-kimyo-texnologiya-instituti-rektori-06-28'>Batafsil...</a></b>"
    )


@dp.message_handler(Text(equals="Ректор"))
async def rector_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Rector_ru.get_fullname()}\n\n"
                f"Должность    |    {Rector_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Rector_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Rector_ru.get_email()}\n\n"
                f"Время приема   |   {Rector_ru.get_reception()}\n\n"
                f"Официальные сайты социальных сетей:\n\n"
                f"<a href='https://t.me/tkti_rektor'>Телеграм</a>    |    <a href='https://www.facebook.com/botir.usmonov.5'>Фейсбук</a>    |    <a href='https://twitter.com/botir2468'>Твиттер</a>\n\n"
                f"<a href='https://telegra.ph/Rektor-Tashkentskogo-himiko-tehnologicheskogo-instituta-07-25'>Подробно...</a></b>"
    )


@dp.message_handler(Text(equals="Rector"))
async def rector_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Rector_en.get_fullname()}\n\n"
                f"Position    |    {Rector_en.get_position()}\n\n"
                f"Contact phone   |   {Rector_en.get_number()}\n\n"
                f"Email address   |   {Rector_en.get_email()}\n\n"
                f"Reception time   |   {Rector_en.get_reception()}\n\n"
                f"Official social networking sites:\n\n"
                f"<a href='https://t.me/tkti_rektor'>Telegram</a>    |    <a href='https://www.facebook.com/botir.usmonov.5'>Facebook</a>    |    <a href='https://twitter.com/botir2468'>Twitter</a>\n\n"
                f"<a href='https://telegra.ph/Rector-of-the-Tashkent-Chemical-Technological-Institute-07-26'>More...</a></b>"
    )
