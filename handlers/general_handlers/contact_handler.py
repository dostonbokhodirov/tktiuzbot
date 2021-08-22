from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot

with open("pictures/tcti.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="☎ Institut bilan aloqa"))
async def contact_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Toshkent kimyo-texnologiya instituti\n\n"
                f"Ishonch telefoni    |    (71) 244-78-49\n\n"
                f"Faks   |   (71) 244-79-17\n\n"
                f"Email manzili   |   info@tcti.uz\n\n"
                f"Exat manzili   |   tcti@exat.uz\n\n"
                f"Batafsil   |   <a href='http://tkti.uz'>Institut rasmiy sayti</a></b>"
    )


@dp.message_handler(Text(equals="☎ Связь с институтом"))
async def contact_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Ташкентский химико-технологический институт\n\n"
                f"Телефон доверия    |    (71) 244-78-49\n\n"
                f"Факс   |   (71) 244-79-17\n\n"
                f"Адрес электронной почты   |   info@tcti.uz\n\n"
                f"Exat адрес   |   tcti@exat.uz\n\n"
                f"Подробно   |   <a href='http://tkti.uz/ru'>Официальный сайт института</a></b>"
    )


@dp.message_handler(Text(equals="☎ Contact with the institute"))
async def contact_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Tashkent Chemical-Technological Institute\n\n"
                f"Helpline    |    (71) 244-78-49\n\n"
                f"Fax   |   (71) 244-79-17\n\n"
                f"Email address   |   info@tcti.uz\n\n"
                f"Exat address   |   tcti@exat.uz\n\n"
                f"More   |   <a href='http://tkti.uz/en'>Official site of the institute</a></b>"
    )
