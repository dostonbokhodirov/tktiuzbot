import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import PKQT_uz, PKQT_ru, PKQT_en

with open("pictures/pkqt.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="TKTI huzuridagi “Pedagogik kadrlani qayta tayyorlash va malaka oshirish” tarmoq markazi"))
async def pkqt_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{PKQT_uz.get_fullname()}\n\n"
                f"Lavozim    |    {PKQT_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {PKQT_uz.get_number()}\n\n"
                f"Email manzil   |   {PKQT_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Tarmoq markazi faoliyati asosan 3 yo‘nalish bo‘yicha faoliyat olib boradi:\n\n"
             f"<i>✅ Oliy ta'lim muassasalarida faoliyat yuritayotgan pedagoglarni belgilangan 5 ta yo‘nalish bo‘yicha malakasini oshirish;\n\n"
             f"✅ Oliy ma'lumotli kadrlarni kasbiy qayta tayyorlash;\n\n"
             f"✅ Ta'lim servisi yo‘nalishi;</i>\n\n\n"
             f"Tarmoq markazida quyidagi bo‘limlar mavjud:\n\n"
             f"<i>✅ Qayta tayyorlash va malaka oshirish ta'lim jarayonini tashkil etish va sifatini o‘rganish bo‘limi\n\n"
             f"✅ Qayta tayyorlash va malaka oshirish ta'lim dasturlari va ilg‘or tajribani joriy etish bo‘limi\n\n"
             f"✅ Xalqaro hamkorlik bo‘limi</i></b>"
    )


@dp.message_handler(Text(equals="Сетевой центр «Переподготовка и повышение квалификации педагогических кадров» при ТКТИ"))
async def pkqt_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{PKQT_ru.get_fullname()}\n\n"
                f"Должность    |    {PKQT_ru.get_position()}\n\n"
                f"Контактный телефон   |   {PKQT_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {PKQT_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Сетевой центр работает по 3 основным направлениям:\n\n"
             f"<i>✅ Повышение квалификации преподавателей высших учебных заведений по 5 направлениям;\n\n"
             f"✅ Профессиональная переподготовка кадров с высшим образованием;\n\n"
             f"✅ Направление образовательных услуг;</i>\n\n\n"
             f"Сетевой центр состоит из следующих разделов:\n\n"
             f"<i>✅ Отдел организации переподготовки и повышения квалификации и исследований качества\n\n"
             f"✅ Департамент программ и передового опыта переподготовки и повышения квалификации\n\n"
             f"✅ Департамент международного сотрудничества</i></b>"
    )


@dp.message_handler(Text(equals="Network center “Retraining and advanced training of teaching staff” at TCTI"))
async def pkqt_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{PKQT_en.get_fullname()}\n\n"
                f"Position    |    {PKQT_en.get_position()}\n\n"
                f"Contact phone   |   {PKQT_en.get_number()}\n\n"
                f"Email address   |   {PKQT_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The network centre operates in 3 main areas:\n\n"
             f"<i>✅ Professional development of teachers working in higher education institutions in 5 areas;\n\n"
             f"✅ Professional retraining of personnel with higher education;\n\n"
             f"✅ Education service direction;</i>\n\n\n"
             f"The network centre has the following sections:\n\n"
             f"<i>✅ Department of retraining and advanced training organization and quality research\n\n"
             f"✅ Department of Retraining and Advanced Training Programs and Best Practices\n\n"
             f"✅ Department of International Cooperation</i></b>"
    )
