from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_union, ru_keyboard_union, en_keyboard_union
from loader import dp, bot

with open("pictures/unionlogo.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Yoshlar Ittifoqi"))
async def union_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Toshkent kimyo-texnologiya instituti Yoshlar Ittifoqi\n\n"
                f"Tashkil etilgan sana    |    2017-yil\n\n"
                f"Manzil    |    <a href='http://bit.ly/tctimap'>TKTI bosh binosi, 410-xona</a>\n\n"
                f"Batafsil    |    <a href='https://t.me/TKTI_Official'>Telegram</a></b>",
        reply_markup=uz_keyboard_union
    )


@dp.message_handler(Text(equals="Союз Молодежи"))
async def union_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Союз молодежи Ташкентского химико-технологического института\n\n"
                f"Дата создания    |    2017 г.\n\n"
                f"Адрес    |    <a href='http://bit.ly/tctimap'>Главный корпус ТКТИ, комната 410</a>\n\n"
                f"Подробно    |    <a href='https://t.me/TKTI_Official'>Телеграм</a></b>",
        reply_markup=ru_keyboard_union
    )


@dp.message_handler(Text(equals="Youth Union"))
async def union_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Youth Union of the Tashkent Chemical-Technological Institute\n\n"
                f"Date of formation    |    2017\n\n"
                f"Address    |    <a href='http://bit.ly/tctimap'>TKTI main building, room 410</a>\n\n"
                f"More    |    <a href='https://t.me/TKTI_Official'>Telegram</a></b>",
        reply_markup=en_keyboard_union
    )
