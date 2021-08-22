import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import ATM_uz, ATM_ru, ATM_en

with open("pictures/atm.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Axborot texnologiyalari markazi"))
async def atm_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ATM_uz.get_fullname()}\n\n"
                f"Lavozim    |    {ATM_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {ATM_uz.get_number()}\n\n"
                f"Email manzil   |   {ATM_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Markazning asosiy vazifalari:\n\n"
             f"<i>✅ Axborot marketingni tashkil etish;\n\n"
             f"✅ Aborot texnologiyalar va multimedia tizimlari sohasidagi ishlarni oliy ta'lim va fani sohalariga tadbiq qilish;\n\n"
             f"✅ Internet tarmog‘i va elektron pochta xizmatlarini ko‘rsatish, aniq mavzular bo‘yicha ma’lumotlarni qidirish va ular joylashgan manzillarni taklif etish;\n\n"
             f"✅ Hisoblash texnikasi vositalariga, kompyuterlarga servis xizmatini tashkil etish, ularni ta'mirlash va modernizatsiyalash;\n\n"
             f"✅ Axborot-kompyuter tarmoqlari va tizimlarini loyihalashtirish, ishga tushirish va sozlash;</i></b>"
    )


@dp.message_handler(Text(equals="Центр информационных технологий"))
async def atm_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ATM_ru.get_fullname()}\n\n"
                f"Должность    |    {ATM_ru.get_position()}\n\n"
                f"Контактный телефон   |   {ATM_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {ATM_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи центра:\n\n"
             f"<i>✅ Организация информационного маркетинга;\n\n"
             f"✅ Применение работ в области информационных технологий и мультимедийных систем в высшем образовании и науке;\n\n"
             f"✅ Предоставлять услуги Интернета и электронной почты, искать информацию по конкретным темам и предлагать их местонахождение;\n\n"
             f"✅ Организация обслуживания, ремонта и модернизации компьютеров, компьютеров;\n\n"
             f"✅ Проектирование, пусконаладка и настройка информационных и компьютерных сетей и систем;</i></b>"
    )


@dp.message_handler(Text(equals="Information Technology Centre"))
async def atm_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ATM_en.get_fullname()}\n\n"
                f"Position    |    {ATM_en.get_position()}\n\n"
                f"Contact phone   |   {ATM_en.get_number()}\n\n"
                f"Email address   |   {ATM_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the centre:\n\n"
             f"<i>✅ Organization of information marketing;\n\n"
             f"✅ Application of work in the field of information technology and multimedia systems in higher education and science;\n\n"
             f"✅ Provide Internet and e-mail services, search for information on specific topics and suggest their addresses;\n\n"
             f"✅ Organization of service, repair and modernization of computers, computers;\n\n"
             f"✅ Design, commissioning and configuration of information and computer networks and systems;</i></b>"
    )
