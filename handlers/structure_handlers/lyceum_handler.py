import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot

with open("pictures/lyceum.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="TKTI qoshidagi akademik litsey"))
async def lyceum_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Toshkent kimyo-texnologiya instituti akademik litseyi\n\n"
                f"Ishonch telefonlari:\n"
                f"(71) 224-87-17   |   (71) 224-88-55   |   (71) 221-61-33\n\n"
                f"Manzil    |    <a href='https://bit.ly/tcti_lyceum'>Toshkent shahri, Yunusobod tumani, 3-mavze, 7-uy</a></b>\n\n\n"
    )

    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Akademik litsey haqida ba'zi ma'lumotlar:\n\n"
             f"<i>Toshkent kimyo-texnologiya instituti akademik litseyiga 2006-yil 2-sentabrda asos solingan.\n\n"
             f"O‘qish muddati ikki yildan iborat.\n\n"
             f"Akademik litsey direktori - Xolmirzayev Zulfiqor Jo‘rayevich</i></b>"
    )


@dp.message_handler(Text(equals="Академический лицей при ТКТИ"))
async def lyceum_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Академический лицей Ташкентского химико-технологического института\n\n"
                f"Телефоны доверия:\n"
                f"(71) 224-87-17   |   (71) 224-88-55   |   (71) 221-61-33\n\n"
                f"Адрес    |    <a href='https://bit.ly/tcti_lyceum'>Город Ташкент, Юнусабадский район, 3 квартал, 7 дом</a></b>\n\n\n"
    )

    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации об академическом лицее:\n\n"
             f"<i>Академический лицей Ташкентского химико-технологического института основан 2 сентября 2006 года.\n\n"
             f"Срок обучения - два года.\n\n"
             f"Директор академического лицея - Холмирзаев Зулфикор Джораевич.</i></b>"
    )


@dp.message_handler(Text(equals="Academic lyceum under TCTI"))
async def lyceum_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Academic Lyceum of the Tashkent Chemical-Technological Institute\n\n"
                f"Helplines:\n"
                f"(71) 224-87-17   |   (71) 224-88-55   |   (71) 221-61-33\n\n"
                f"Address    |    <a href='https://bit.ly/tcti_lyceum'>Tashkent, Yunusabad district, 3rd district, 7th house</a></b>\n\n\n"
    )

    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the academic lyceum:\n\n"
             f"<i>The Academic Lyceum of the Tashkent Chemical-Technological Institute was founded on September 2, 2006.\n\n"
             f"Duration of study is two years.\n\n"
             f"The director of the academic lyceum is Kholmirzaev Zulfiqor Jorayevich</i></b>"
    )
