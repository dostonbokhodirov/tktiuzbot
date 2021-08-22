import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Kadrlar_uz, Kadrlar_ru, Kadrlar_en

with open("pictures/kadrlar.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Kadrlar bo‘limi"))
async def kadrlar_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Kadrlar_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Kadrlar_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Kadrlar_uz.get_number()}\n\n"
                f"Email manzil   |   {Kadrlar_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Institut rаhbаriyati vа bo‘lim boshliqlаri bilаn “Kаdrlаr tаyyorlаsh milliy dаsturi”gа muvofiq zаmonаviy tаlаblаrgа jаvob beruvchi kаdrlаr tаyyorlаsh jаrаyoni uchun lаyoqаtli, yuqori mаlаkаli, chuqur kаsbiy bilimgа egа, ilmiy yutuqlаrgа erishgаn ijodiy-ilmiy sаlohiyatli, yuqori idrok vа аxloqli xodimlаrni tаnlаsh-sаrаlаsh, ishgа qаbul qilish;\n\n"
             f"✅ Professor-o‘qituvchi, o‘quv-yordаmchi vа mа'muriy-xo‘jаlik xodimlаrni mehnаt shаrtnomаsi аsosidа ishgа qаbul qilish, boshqа lаvozimgа o‘tkаzish vа ishdаn ozod qilish to‘g‘risidаgi hujjаtlаrni rаsmiylаshtirish;\n\n"
             f"✅ Mehnаt dаftаrchаlаrini sаqlаsh, to‘ldirish, kаdrlаr bo‘yichа belgilаngаn hujjаtlаrni rаsmiylаshtirish;\n\n"
             f"✅ Tа'tilgа chiqish grаfiklаrini tuzish vа uning bаjаrilishini nаzorаt qilish;\n\n"
             f"✅ Institut xodimlаri bo‘yichа mа'lumotlаr bаzаsini shаklаntirish vа doimiy yangilаb borish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел кадров"))
async def kadrlar_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Kadrlar_ru.get_fullname()}\n\n"
                f"Должность    |    {Kadrlar_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Kadrlar_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Kadrlar_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Подбор квалифицированных, высококвалифицированных, обладающих глубокими профессиональными знаниями, творческим и научным потенциалом, высоким интеллектом и нравственностью для процесса подготовки кадров, отвечающих современным требованиям, в соответствии с «Национальной программой подготовки кадров» под руководством института и руководителями отделы, подбор персонала;\n\n"
             f"✅ Оформление документов о приеме на работу, переводе и увольнении профессоров, преподавателей и административного персонала на основании трудовых договоров;\n\n"
             f"✅ Хранение, пополнение трудовых книжек, оформление кадровых документов;\n\n"
             f"✅ Создание графиков отпусков и контроль его выполнения;\n\n"
             f"✅ Формирование и постоянное обновление базы данных сотрудников института;</i></b>"
    )


@dp.message_handler(Text(equals="Personnel Department"))
async def kadrlar_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Kadrlar_en.get_fullname()}\n\n"
                f"Position    |    {Kadrlar_en.get_position()}\n\n"
                f"Contact phone   |   {Kadrlar_en.get_number()}\n\n"
                f"Email address   |   {Kadrlar_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Selection of qualified, highly qualified, with deep professional knowledge, creative and scientific potential, high intelligence and morality for the process of training personnel meeting modern requirements in accordance with the “National Program of Personnel Training” with the leadership of the Institute and heads of departments, recruitment;\n\n"
             f"✅ Execution of documents on employment, transfer and dismissal of professors, teaching assistants and administrative staff on the basis of employment contracts;\n\n"
             f"✅ Storage, replenishment of employment records, registration of personnel documents;\n\n"
             f"✅ Creating vacation schedules and monitoring its implementation;\n\n"
             f"✅ Forming and constantly updating the database of the Institute's staff;</i></b>"
    )
