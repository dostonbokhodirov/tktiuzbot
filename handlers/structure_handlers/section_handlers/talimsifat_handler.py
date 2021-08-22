import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Talimsifat_uz, Talimsifat_ru, Talimsifat_en

with open("pictures/talimsifat.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Ta'lim sifatini nazorat qilish bo‘limi"))
async def talimsifat_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Talimsifat_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Talimsifat_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Talimsifat_uz.get_number()}\n\n"
                f"Email manzil   |   {Talimsifat_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Davlat inspeksiyasiga taqdim qilinayotgan ma'lumotlarning haqqoniyligiga hamda ishchi o‘quv rejalari va fanlarning ishchi dasturlarini tayyorlash sifati, bitiruvchilarning yakuniy attestatsiya va reyting baholari xolisligini belgilangan tartibda nazoratini tashkil etishga javob berish;\n\n"
             f"✅ TKTI talabalari bilimlarining davlat ta’lim standartlariga muvofiqligini o‘rganib borish, tahlil qilish, kadrlar tayyorlash sifati monitoringini yuritish;\n\n"
             f"✅ TKTIni ichki attestatsiyadan o‘tkazishni tashkil etish va uning natijalari bo‘yicha ta’lim sifatiga salbiy ta’sir etuvchi omillarni aniqlash hamda ularni bartaraf etish va oldini olish choralarini ko‘rish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел контроля качества образования"))
async def talimsifat_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Talimsifat_ru.get_fullname()}\n\n"
                f"Должность    |    {Talimsifat_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Talimsifat_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Talimsifat_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Ответственность за достоверность информации, предоставляемой Государственной инспекции, и организацию контроля за качеством подготовки рабочих учебных планов и рабочих программ дисциплин, объективности итоговой аттестации и рейтинга выпускников;\n\n"
             f"✅ Изучать и анализировать соответствие знаний студентов ТКТИ государственным образовательным стандартам, контролировать качество обучения;\n\n"
             f"✅ Организовать внутреннюю аттестацию ТКТИ и по ее результатам выявить факторы, негативно влияющие на качество образования, и принять меры по их устранению и предупреждению;</i></b>"
    )


@dp.message_handler(Text(equals="Education quality control Department"))
async def talimsifat_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Talimsifat_en.get_fullname()}\n\n"
                f"Position    |    {Talimsifat_en.get_position()}\n\n"
                f"Contact phone   |   {Talimsifat_en.get_number()}\n\n"
                f"Email address   |   {Talimsifat_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Responsibility for the accuracy of the information provided to the State Inspectorate and the organization of control over the quality of preparation of working curricula and working programs of disciplines, the objectivity of the final certification and rating of graduates;\n\n"
             f"✅ To study and analyze the compliance of the knowledge of TCTI students with the state educational standards, to monitor the quality of training;\n\n"
             f"✅ Organize the internal certification of TCTI and identify the factors that negatively affect the quality of education based on its results and take measures to eliminate and prevent them;</i></b>"
    )
