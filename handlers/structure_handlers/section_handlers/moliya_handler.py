import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Moliya_uz, Moliya_ru, Moliya_en

with open("pictures/man.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Reja-moliya bo‘limi"))
async def moliya_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Moliya_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Moliya_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Moliya_uz.get_number()}\n\n"
                f"Email manzil   |   {Moliya_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Institut moliyaviy faoliyatini rejalashtirish va tashkil etilishini nazorat qilish;\n\n"
             f"✅ Institut ishchi-xodimlarini rag’batlantirishda ishtirok etish;\n\n"
             f"✅ Institut xodimlarini bazaviy lavozim maoshlarining tasdiqlangan razryad va tarif koeffitsentlariga mosligini muntazam nazorat qilib borish;\n\n"
             f"✅ Moliyaviy faoliyatning barcha turlari bo‘yicha istiqbolli va yillik daromadlar hamda smetasini tuzish, ular ijrosini ta'minlash;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел планирования и финансов"))
async def moliya_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Moliya_ru.get_fullname()}\n\n"
                f"Должность    |    {Moliya_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Moliya_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Moliya_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Контроль за планированием и организацией финансовой деятельности Института;\n\n"
             f"✅ Участвовать в мотивации сотрудников Института;\n\n"
             f"✅ Регулярный контроль за соответствием должностных окладов сотрудников Института утвержденным разрядным и тарифным коэффициентам;\n\n"
             f"✅ Составление прогнозных и годовых доходов и смет по всем видам финансовой деятельности, обеспечение их реализации;</i></b>"
    )


@dp.message_handler(Text(equals="Planning and Finance Department"))
async def moliya_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Moliya_en.get_fullname()}\n\n"
                f"Position    |    {Moliya_en.get_position()}\n\n"
                f"Contact phone   |   {Moliya_en.get_number()}\n\n"
                f"Email address   |   {Moliya_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Control over the planning and organization of financial activities of the Institute;\n\n"
             f"✅ Participate in motivating employees of the Institute;\n\n"
             f"✅ Regular monitoring of compliance of basic salaries of employees of the Institute with the approved discharge and tariff coefficients;\n\n"
             f"✅ Preparation and estimation of prospective and annual revenues and estimates for all types of financial activities, ensuring their implementation;</i></b>"
    )
