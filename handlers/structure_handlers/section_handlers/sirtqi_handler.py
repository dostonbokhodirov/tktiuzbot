import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Sirtqi_uz, Sirtqi_ru, Sirtqi_en

with open("pictures/sirtqi.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Sirtqi bo‘lim"))
async def sirtqi_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Sirtqi_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Sirtqi_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Sirtqi_uz.get_number()}\n\n"
                f"Email manzil   |   {Sirtqi_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Sirtqi ta’limni rivojlantirish dasturlarini ishlab chiqish;\n\n"
             f"✅ Talabalarning malakaviy amaliyotlarini tashkil qilish bo‘yicha ish beruvchilar bilan shartnomalar tuzish;\n\n"
             f"✅ O‘qitishning yangi texnologiyalari tatbiq qilinishini va talabalar o‘zlashtirishi nazorat qilinishini ta’minlash;\n\n"
             f"✅ Talabalarning bitiruv malakaviy ishlari mavzularini muvofiqlashtirish va tasdiqlash;\n\n"
             f"✅ Talabalar bilan o‘quv va tarbiyaviy ishlar olib borish samaradorligini oshirish choralarini ko‘rish;</i></b>"
    )


@dp.message_handler(Text(equals="Заочный отделение"))
async def sirtqi_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Sirtqi_ru.get_fullname()}\n\n"
                f"Должность    |    {Sirtqi_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Sirtqi_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Sirtqi_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Разработка развивающих программ дистанционного обучения;\n\n"
             f"✅ Договоры с работодателями на организацию стажировок студентов;\n\n"
             f"✅ Обеспечение внедрения новых технологий обучения и мониторинг обучения студентов;\n\n"
             f"✅ Согласование и утверждение тем для выпускной работы;\n\n"
             f"✅ Принимать меры по повышению эффективности учебно-воспитательной работы со студентами;</i></b>"
    )


@dp.message_handler(Text(equals="Correspondence Department"))
async def sirtqi_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Sirtqi_en.get_fullname()}\n\n"
                f"Position    |    {Sirtqi_en.get_position()}\n\n"
                f"Contact phone   |   {Sirtqi_en.get_number()}\n\n"
                f"Email address   |   {Sirtqi_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Development of distance learning development programs;\n\n"
             f"✅ Contracts with employers for the organization of student internships;\n\n"
             f"✅ Ensuring the introduction of new teaching technologies and monitoring student learning;\n\n"
             f"✅ Coordination and approval of topics for graduate work of students;\n\n"
             f"✅ Take measures to increase the effectiveness of teaching and educational work with students;</i></b>"
    )
