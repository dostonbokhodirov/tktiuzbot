import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Manaviyat_uz, Manaviyat_ru, Manaviyat_en

with open("pictures/manaviyat.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Yoshlar bilan ishlash, ma'naviyat va ma'rifat bo‘limi"))
async def manaviyat_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Manaviyat_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Manaviyat_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Manaviyat_uz.get_number()}\n\n"
                f"Email manzil   |   {Manaviyat_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Mamlakatimizda amalga oshirilayotgan ma’naviy, madaniy ishlarga doir tadbirlarni o‘tkazish;\n\n"
             f"✅ Talaba-yoshlar orasida axloqiy, estetik, siyosiy, huquqiy, badiiy tarbiyani shakllantirish ishlarini yo‘lga qo‘yish;\n\n"
             f"✅ Milliy urf-odatlar, qadriyatlar negizida olib borilayotgan anjumanlar, davra suhbatlari, uchrashuvlarni tashkil etish;\n\n"
             f"✅ Talabalarning ma'naviy va jismoniy kamolotini yuksaltirish maqsadida qilinadigan ishlarni takomillashtirishga ko‘maklashish;\n\n"
             f"✅ Institutda ma'naviy, ma'rifiy va tarbiyaviy ishlarning ustuvor yo‘nalishlarini belgilash, bu borada zarur me'yoriy hujjatlar va tavsiyanomalarni ishlab chiqish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел по делам молодежи, духовности и просвещения"))
async def manaviyat_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Manaviyat_ru.get_fullname()}\n\n"
                f"Должность    |    {Manaviyat_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Manaviyat_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Manaviyat_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Проведение мероприятий по духовной, культурной работе, проводимой в нашей стране;\n\n"
             f"✅ Организовать формирование нравственного, эстетического, политического, правового, художественного воспитания студентов;\n\n"
             f"✅ Организация конференций, круглых столов, встреч на основе национальных традиций и ценностей;\n\n"
             f"✅ Помощь в улучшении проделанной работы по улучшению духовного и физического развития студентов;\n\n"
             f"✅ Определение приоритетов духовной, воспитательной и педагогической работы в институте, разработка необходимых положений и рекомендаций по этому поводу;</i></b>"
    )


@dp.message_handler(Text(equals="Department of Youth Affairs, Spirituality and Education"))
async def manaviyat_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Manaviyat_en.get_fullname()}\n\n"
                f"Position    |    {Manaviyat_en.get_position()}\n\n"
                f"Contact phone   |   {Manaviyat_en.get_number()}\n\n"
                f"Email address   |   {Manaviyat_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Carrying out of actions on spiritual, cultural work carried out in our country;\n\n"
             f"✅ To organize the formation of moral, aesthetic, political, legal, artistic education among students;\n\n"
             f"✅ Organization of conferences, roundtables, meetings based on national traditions and values;\n\n"
             f"✅ Helping to improve the work done to improve the spiritual and physical development of students;\n\n"
             f"✅ Establishing the priorities of spiritual, educational and pedagogical work at the Institute, the development of the necessary regulations and recommendations in this regard;</i></b>"
    )
