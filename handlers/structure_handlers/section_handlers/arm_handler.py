import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import ARM_uz, ARM_ru, ARM_en

with open("pictures/arm.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Axborot-resurs markazi"))
async def arm_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ARM_uz.get_fullname()}\n\n"
                f"Lavozim    |    {ARM_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {ARM_uz.get_number()}\n\n"
                f"Email manzil   |   {ARM_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Markazning asosiy vazifalari:\n\n"
             f"<i>✅ Axborot texnologiyalaridan foydalangan holda foydalanuvchilarning muntazam ta'lim olishga va mustaqil ravishda ta'lim olishga ko‘maklashish;\n\n"
             f"✅ Axborotlarga bo‘lgan talablarga muvofiq va ARM ma'lumotlar qidirish apparati tizimi orqali har qanday fondlardan keng foydalangan holda yangi axborot texnologiyalari asosida talabalarga zarur darajada axborot xizmati ko‘rsatish;\n\n"
             f"✅ Internet tarmog‘i va elektron pochta xizmatlarini ko‘rsatish, aniq mavzular bo‘yicha ma’lumotlarni qidirish va ular joylashgan manzillarni taklif etish;\n\n"
             f"✅ Intellektual faoliyat bo‘yicha bilimlar, g‘oyalar, ilmiy va amaliy natijalarni erkin almashish;</i></b>"
    )


@dp.message_handler(Text(equals="Информационно-ресурсный центр"))
async def arm_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ARM_ru.get_fullname()}\n\n"
                f"Должность    |    {ARM_ru.get_position()}\n\n"
                f"Контактный телефон   |   {ARM_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {ARM_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи центра:\n\n"
             f"<i>✅ Содействовать регулярному обучению и независимому обучению с помощью информационных технологий;\n\n"
             f"✅ Предоставлять студентам необходимые информационные услуги на основе новых информационных технологий в соответствии с требованиями к информации и с широким использованием любых средств через информационно-поисковую систему ИРЦ;\n\n"
             f"✅ Предоставлять услуги Интернета и электронной почты, искать информацию по конкретным темам и предлагать их местонахождение;\n\n"
             f"✅ Свободный обмен знаниями, идеями, научными и практическими результатами в интеллектуальной деятельности;</i></b>"
    )


@dp.message_handler(Text(equals="Information Resource Centre"))
async def arm_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{ARM_en.get_fullname()}\n\n"
                f"Position    |    {ARM_en.get_position()}\n\n"
                f"Contact phone   |   {ARM_en.get_number()}\n\n"
                f"Email address   |   {ARM_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the centre:\n\n"
             f"<i>✅ Free exchange of knowledge, ideas, scientific and practical results in intellectual activity;\n\n"
             f"✅ To provide students with the necessary information services on the basis of new information technologies in accordance with the requirements for information and with the extensive use of any funds through the IRC information retrieval system;\n\n"
             f"✅ Provide Internet and e-mail services, search for information on specific topics and suggest their addresses;\n\n"
             f"✅ Free exchange of knowledge, ideas, scientific and practical results in intellectual activity;</i></b>"
    )
