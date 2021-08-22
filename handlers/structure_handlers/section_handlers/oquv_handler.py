import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Oquv_uz, Oquv_ru, Oquv_en

with open("pictures/oquv.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="O‘quv-uslubiy bo‘lim"))
async def oquv_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Oquv_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Oquv_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Oquv_uz.get_number()}\n\n"
                f"Email manzil   |   {Oquv_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Institut o‘quv jarayonini rejalashtirish, tashkillashtirish, muvofiqlashtirish va nazorat olib borish;\n\n"
             f"✅ Institut fakultetlari va kafedralariga o’quv rejalari va o’quv dasturlarini ishlab chiqishda amaliy yordam ko’rsatish;\n\n"
             f"✅ Fakultetlar va kafedralarning o’quv-uslubiy ishlarini  muvofiqlashitish va uni boshqarishdagi me'yoriy hujjatlarini doimiy  takomillashtirish;\n\n"
             f"✅ Institut ta'limini rivojlantirish uchun istiqbolli rejalarni ishlab chiqish va institut Kengashiga tavsiya qilish;\n\n"
             f"✅ O‘quv jarayoni va talabalar faoliyatiga oid barcha tashkiliy, o‘quv-uslubiy ishlarni amalga oshirish;</i></b>"
    )


@dp.message_handler(Text(equals="Учебно-методический отдел"))
async def oquv_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Oquv_ru.get_fullname()}\n\n"
                f"Должность    |    {Oquv_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Oquv_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Oquv_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Планирование, организация, координация и контроль учебного процесса института;\n\n"
             f"✅ Оказывать практическую помощь факультетам и кафедрам института в разработке учебных планов и программ обучения;\n\n"
             f"✅ Постоянное совершенствование нормативных документов в области координации и управления учебно-методической работой факультетов и кафедр;\n\n"
             f"✅ IРазработка перспективных планов развития образования Института и рекомендация Совету Института;\n\n"
             f"✅ Осуществлять всю организационную, учебно-методическую работу, связанную с учебным процессом и деятельностью студентов;</i></b>"
    )


@dp.message_handler(Text(equals="Educational-methodical Department"))
async def oquv_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Oquv_en.get_fullname()}\n\n"
                f"Position    |    {Oquv_en.get_position()}\n\n"
                f"Contact phone   |   {Oquv_en.get_number()}\n\n"
                f"Email address   |   {Oquv_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Planning, organizing, coordinating and supervising the educational process of the institute;\n\n"
             f"✅ Provide practical assistance to faculties and departments of the Institute in the development of curricula and study programs;\n\n"
             f"✅ Continuous improvement of regulatory documents in the coordination and management of educational and methodological work of faculties and departments;\n\n"
             f"✅ Development of perspective plans for the development of education of the Institute and recommendation to the Council of the Institute;\n\n"
             f"✅ Carry out all organizational, educational and methodological work related to the educational process and student activities;</i></b>"
    )
