import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Monitoring_uz, Monitoring_ru, Monitoring_en

with open("pictures/monitoring.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Monitoring va ichki nazorat bo‘limi"))
async def monitoring_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Monitoring_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Monitoring_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Monitoring_uz.get_number()}\n\n"
                f"Email manzil   |   {Monitoring_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Bo‘limning asosiy vazifasi O‘zbekiston Respublikasi Qonunlari, O‘zbekiston Respublikasi Prezidenti Farmonlari, qarorlari va farmoyishlari, O‘zbekiston Respublikasi Vazirlar Mahkamasi qarorlari va farmoyishlari, O‘zbekiston Respublikasi Oliy va o‘rta maxsus ta’lim vazirligi Hay’ati qarorlari, vazir buyruqlari, topshiriq va xat-hujjatlari hamda institut Kengashi qarorlari,  Jismoniy va yuridik shaxslarning murojaatlari, institut rektori buyruq va topshiriqlari ijrolarini monitoringini va nazoratini olib borish, har oy va har chorakda vazirlikka hisobot tayyorlash hamda bu asosiy vazifa bo‘yicha institut Kengashida axborot berib borish;\n\n"
             f"✅ Institut Kengashi qarori bilan tasdiqlangan yillik ish rejaga asosan Bo‘lim tomonidan institut kafedralari va bo‘limlari faoliyatini har oyda maqsadli o‘rganish o‘tkaziladi va o‘rganish natijalari institut Kengashi yig‘ilishida muhokamaga qo‘yiladi;\n\n"
             f"✅ Institutda O‘zbekiston Respublikasining oliy ta’limga oid qonunlari, vazirlikning Hay’at qarori, buyruqlari va boshqa hujjatlarini, shuningdek institut ichki buyruqlari va qarorlarining bajarilishi monitoringini olib borish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел мониторинга и внутреннего контроля"))
async def monitoring_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Monitoring_ru.get_fullname()}\n\n"
                f"Должность    |    {Monitoring_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Monitoring_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Monitoring_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Основными задачами отдела являются законы Республики Узбекистан, указы, постановления и распоряжения Президента Республики Узбекистан, постановления и распоряжения Кабинета Министров Республики Узбекистан, постановления Коллегии Министерства. высшего и среднего специального образования, мониторинг и контроль за исполнением приказов, поручений и писем Министра и решений Совета института, обращений физических и юридических лиц, приказов и распоряжений ректора института, подготовка ежемесячные и ежеквартальные отчеты в министерство и информация по этой основной задаче;\n\n"
             f"✅ Согласно годовому плану работы, утвержденному решением Совета института, кафедра ежемесячно проводит целевое изучение деятельности кафедр и подразделений института, а результаты исследования обсуждаются на заседании института;\n\n"
             f"✅ Контроль за исполнением законов Республики Узбекистан о высшем образовании, решений, приказов и других документов Коллегии Министерства, а также внутренних приказов и решений Института;</i></b>"
    )


@dp.message_handler(Text(equals="Monitoring and Internal Control Department"))
async def monitoring_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Monitoring_en.get_fullname()}\n\n"
                f"Position    |    {Monitoring_en.get_position()}\n\n"
                f"Contact phone   |   {Monitoring_en.get_number()}\n\n"
                f"Email address   |   {Monitoring_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ The main tasks of the department are the laws of the Republic of Uzbekistan, decrees, resolutions and orders of the President of the Republic of Uzbekistan, resolutions and orders of the Cabinet of Ministers of the Republic of Uzbekistan, resolutions of the Board of the Ministry of Higher and Secondary Special Education , monitoring and control over the implementation of orders, instructions and letters of the Minister and decisions of the Council of the Institute, appeals of individuals and legal entities, orders and instructions of the Rector of the Institute, preparation of monthly and quarterly reports to the Ministry and information on this main task give and take;\n\n"
             f"✅ According to the annual work plan approved by the decision of the Council of the Institute, the Department conducts a monthly targeted study of the activities of departments and divisions of the Institute, and the results of the study are discussed at a meeting of the Institute;\n\n"
             f"✅ Monitoring the implementation of the laws of the Republic of Uzbekistan on higher education, resolutions, orders and other documents of the Board of the Ministry, as well as internal orders and decisions of the institute;</i></b>"
    )
