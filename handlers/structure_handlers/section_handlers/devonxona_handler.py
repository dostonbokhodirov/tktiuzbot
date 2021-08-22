import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Devonxona_uz, Devonxona_ru, Devonxona_en

with open("pictures/woman.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Devonxona va arxiv bo‘limi"))
async def devonxona_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Devonxona_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Devonxona_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Devonxona_uz.get_number()}\n\n"
                f"Email manzil   |   {Devonxona_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Devonxonaga kelib tushadigan farmonlar, qarorlar, buyruqlar, xatlar va boshqa hujjatlarni o‘z vaqtida belgilangan tartibda qabul qilish, rasmiylashtirish va institut rahbariyatiga, so‘ngra institut tarkibiy qismlardagi ijrochilarga yetkazish hamda tegishli tartibda, rahbariyatga ma’lumot berib borish;\n\n"
             f"✅ Devonxonaga kelib tushadigan hujjatlarni ijro muddati institut rahbariyati tomonidan belgilangach uni o‘z vaqtida ijrochilarga tarqatib, nazoratda ekanligini eslatib o‘tadi va Monitoring va ichki nazorat bo‘limiga axborot beradi;\n\n"
             f"✅ Rahbariyat tomonidan berilayotgan ko‘rsatmalar, farmoyishlar, buyruq va topshiriqnomalarni rasmiylashtiradi, ijrosini ta’minlaydi va  chiqarayotgan barcha hujjatlarni sifati uchun javobgarlik mas’uliyatini ta’minlaydi;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел канцелярия и архив"))
async def devonxona_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Devonxona_ru.get_fullname()}\n\n"
                f"Должность    |    {Devonxona_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Devonxona_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Devonxona_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Принимать, оформлять и своевременно передавать поступившие Кабинетом министров постановления, решения, приказы, письма и другие документы руководству института, а затем исполнителям компонентов института и, соответственно, информировать руководство;\n\n"
             f"✅ После того, как срок оформления поступивших в офис документов установлен руководством института, он своевременно раздает их исполнителям, напоминает им, что находится на контроле, и информирует Департамент мониторинга и внутреннего контроля;\n\n"
             f"✅ Выполняет инструкции, приказы, распоряжения и поручения руководства, обеспечивает их выполнение и несет ответственность за качество всех выданных документов;</i></b>"
    )


@dp.message_handler(Text(equals="Chancellery and Archives Department"))
async def devonxona_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Devonxona_en.get_fullname()}\n\n"
                f"Position    |    {Devonxona_en.get_position()}\n\n"
                f"Contact phone   |   {Devonxona_en.get_number()}\n\n"
                f"Email address   |   {Devonxona_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Receipt, execution and timely delivery of decrees, decisions, orders, letters and other documents received by the Office to the management of the institute, and then to the executors of the components of the institute and, accordingly, to the management;\n\n"
             f"✅ Once the deadline for the execution of documents received by the office is set by the management of the institute, it distributes it to the executors in a timely manner, reminds that it is under control and informs the Department of Monitoring and Internal Control;\n\n"
             f"✅ Executes instructions, orders, directives and assignments issued by management, ensures their execution and is responsible for the quality of all documents issued;</i></b>"
    )
