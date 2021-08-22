import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_filial_y, ru_keyboard_filial_y, en_keyboard_filial_y
from loader import dp, bot

with open("pictures/yangiyer.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="TKTI Yangiyer filiali"))
async def filial_sh_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Toshkent kimyo-texnologiya instituti Yangiyer filiali\n\n"
                f"Ishonch telefoni    |    (95) 510-58-56\n\n"
                f"Email manzil   |   tktiyaf@tcti.uz\n\n"
                f"Manzil    |    <a href='https://bit.ly/filial_yangiyer'>Sirdaryo viloyati, Yangiyer shahri, Tinchlik ko‘chasi, 1-uy</a>\n\n\n"
                f"Batafsil ma'lumotlarni quyidagi manzillar orqali ham olishingiz mumkin:\n\n"
                f"<a href='http://tktiyf.uz'>Rasmiy sayt</a>    |    <a href='https://www.instagram.com/tkti_yaf'>Instagram</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Filial haqida ba'zi ma'lumotlar:\n\n"
             f"<i>O‘z. Res. Vazirlar Mahkamasining 2019-yil 9-iyuldagi 573-sonli qaroriga asosan Yangiyer qurilishi va kommunla xo‘jalik kasb-hunar kolleji o‘rnida Toshkent kimyo-texnologiya institutining Yangiyer filiali tashkil etilgan.\n\n"
             f"Filialda 4 ta ta'lim yo‘nalishi bo‘yicha talabalar o‘qitilib kelinmoqda:\n\n"
             f"✅ Kimyoviy texnologiya (noorganik moddalar kimyoviy texnologiyasi)\n"
             f"✅ Kimyoviy texnologiya (qurilish materiallari texnologiyasi)\n"
             f"✅ Texnologik mashina va jihozlar (kimyo sanoati)\n"
             f"✅ Texnologik jarayonlar va ishlab chiqarishni avtomatlashtirish va boshqaruv (tarmoqlar bo‘yicha)</i></b>",
        reply_markup=uz_keyboard_filial_y
    )


@dp.message_handler(Text(equals="ТКТИ Янгиерский филиал"))
async def filial_sh_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Янгиерский филиал Ташкентского химико-технологического института\n\n"
                f"Телефон доверия    |    (95) 510-58-56\n\n"
                f"Адрес электронной почты   |   tktiyaf@tcti.uz\n\n"
                f"Адрес    |    <a href='https://bit.ly/filial_yangiyer'>Сырдарьинская область, город Янгиер, улица Тинчлик, 1</a>\n\n\n"
                f"Вы также можете получить дополнительную информацию по следующим адресам:\n\n"
                f"<a href='http://tktiyf.uz'>Официальный сайт</a>    |    <a href='https://www.instagram.com/tkti_yaf'>Инстаграм</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о филиале:\n\n"
             f"<i>Постановлением Кабинета Министров Республики Узбекистан № 573 от 9 июля 2019 года на базе Янгиерского профессионального колледжа строительства и коммунального хозяйства создан Янгиерский филиал Ташкентского химико-технологического института.\n\n"
             f"Филиал обучает студентов по 4 направлениям:\n\n"
             f"✅ Химическая технология (химическая технология неорганических веществ)\n"
             f"✅ Химическая технология (технология строительных материалов)\n"
             f"✅ Технологические машины и оборудование (химическая промышленность)\n"
             f"✅ Технологические процессы и автоматизация и управление производством (по отраслям)</i></b>",
        reply_markup=ru_keyboard_filial_y
    )


@dp.message_handler(Text(equals="Yangiyer branch of TCTI"))
async def filial_sh_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Yangier branch of the Tashkent Chemical-Technological Institute\n\n"
                f"Helpline    |    (95) 510-58-56\n\n"
                f"Email address   |   tktiyaf@tcti.uz\n\n"
                f"Address    |    <a href='https://bit.ly/filial_yangiyer'>Syrdarya region, Yangiyer city, Tinchlik street, 1</a>\n\n\n"
                f"You can also get more information at the following addresses:\n\n"
                f"<a href='http://tktiyf.uz'>Official site</a>    |    <a href='https://www.instagram.com/tkti_yaf'>Instagram</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the branch:\n\n"
             f"<i>By the Decree of the Cabinet of Ministers of the Republic of Uzbekistan No. 573 of July 9, 2019, the Yangier branch of the Tashkent Chemical-Technological Institute was established on the basis of the Yangiyorsk Professional College of Construction and Utilities.\n\n"
             f"The branch teaches students in 4 fields of study:\n\n"
             f"✅ Chemical technology (chemical technology of inorganic substances)\n"
             f"✅ Chemical technology (building materials technology)\n"
             f"✅ Technological machines and equipment (chemical industry)\n"
             f"✅ Technological processes and production automation and management (by industry)</i></b>",
        reply_markup=en_keyboard_filial_y
    )
