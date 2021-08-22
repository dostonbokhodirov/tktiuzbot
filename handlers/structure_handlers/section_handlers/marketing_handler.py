import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Marketing_uz, Marketing_ru, Marketing_en

with open("pictures/marketing.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Marketing bo‘limi"))
async def monitoring_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Marketing_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Marketing_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Marketing_uz.get_number()}\n\n"
                f"Email manzil   |   {Marketing_uz.get_email()}\n\n"
                f"Telegram    |    <a href='https://t.me/tktimarket'>TCTI Market</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Mehnat bozori konyukturasini o’rganish va talabalar qabuli ko’rsatkichlarini aniqlash maqsadida ish beruvchilar (korxona va tashkilotlar)ning mavjud ta’lim yo‘nalishlari yoki mutaxassisliklarga bo‘lgan talablari (buyurtmalar)ni hisobga olgan holda davlat grantlari va to’lov-shartnoma bo’yicha joriy va istiqbolli «buyurtmalar portfeli»ni shakllantirish;\n\n"
             f"✅ Yangi o‘quv yili qabul rejasining bajarilishi (davlat grantlari va to’lov-shartnoma bo’yicha qabul rejasi, tushgan arizalar, tanlov, qabul qilingan talabalar soni va bosqichlari, ta’lim yo‘nalishlari) bo‘yicha ma’lumotlar bankini yaratish;\n\n"
             f"✅ Bakalavriat yo‘nalishlari, magistratura mutaxassisliklari bo‘yicha talabalarning kasbiy mahoratini oshirish vа bitiruvchilarni ishga taqsimlash borasida institutning tegishli bo‘linmalar bilan hamkorlik qilish;\n\n"
             f"✅ Mutaxassislar tayyorlash bo‘yicha korxona, muassasa, tashkilotlar, jismoniy shaxslar bilan shartnomalarni rasmiylashtirish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел маркетинга"))
async def monitoring_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Marketing_ru.get_fullname()}\n\n"
                f"Должность    |    {Marketing_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Marketing_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Marketing_ru.get_email()}\n\n"
                f"Телеграм    |    <a href='https://t.me/tktimarket'>TCTI Market</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ В целях изучения ситуации на рынке труда и определения показателей приема студентов, государственных грантов и договоров оплаты труда с учетом требований (заказов) работодателей (предприятий и организаций) к существующим направлениям обучения или формированию специальностей текущих и будущий «портфель заказов»\n\n"
             f"✅ Создание базы данных о выполнении плана приема на новый учебный год (план приема по государственным грантам и платежным договорам, заявки, конкурс, количество и этапы приема студентов, направления обучения);\n\n"
             f"✅ Сотрудничать с профильными подразделениями института по повышению квалификации студентов бакалавриата и магистратуры и трудоустройству выпускников;\n\n"
             f"✅ Заключение договоров с предприятиями, учреждениями, организациями, частными лицами на подготовку специалистов;</i></b>"
    )


@dp.message_handler(Text(equals="Marketing Department"))
async def monitoring_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Marketing_en.get_fullname()}\n\n"
                f"Position    |    {Marketing_en.get_position()}\n\n"
                f"Contact phone   |   {Marketing_en.get_number()}\n\n"
                f"Email address   |   {Marketing_en.get_email()}\n\n"
                f"Telegram    |    <a href='https://t.me/tktimarket'>TCTI Market</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ In order to study the situation on the labor market and determine the indicators of student enrollment, state grants and payment agreements, taking into account the requirements (orders) of employers (enterprises and organizations) for existing fields of study or specialties formation of current and future “order portfolio”\n\n"
             f"✅ Creating a database on the implementation of the admission plan for the new academic year (admission plan for state grants and payment-contracts, applications, competitions, number and stages of admission, areas of study);\n\n"
             f"✅ Collaborate with relevant departments of the institute to improve the professional skills of students in bachelor's and master's specialities and the employment of graduates;\n\n"
             f"✅ Execution of contracts with enterprises, institutions, organizations, individuals for the training of specialists;</i></b>"
    )
