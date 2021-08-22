import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Buxgalteriya_uz, Buxgalteriya_ru, Buxgalteriya_en

with open("pictures/woman.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Buxgalteriya bo‘limi"))
async def buxgalteriya_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Buxgalteriya_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Buxgalteriya_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Buxgalteriya_uz.get_number()}\n\n"
                f"Email manzil   |   {Buxgalteriya_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ O‘zbekiston Respublikasi Moliya vazirligi tomonidan tasdiqlangan me’yoriy hujjatlarga asosan buxgalteriya hisobini tashkil qilishni ta’minlash, moddiy, mehnat va moliyaviy resurslaridan samarali foydalanishni nazorat qilish;\n\n"
             f"✅ Professor-o‘qituvchi va xodimlar oylik ish haqlarini, talabalar stipendiyalarini o‘z vaqtida hisoblashni va ularni tarqatilishini nazorat qilish;\n\n"
             f"✅ Hisob varaqalarda aktivlarning holatini va harakatini, mulkiy huquqlar va majburiyatlarning holati to‘g‘risidagi to‘liq xamda aniq ma’lumotlarni shakllantirish;\n\n"
             f"✅ Moddiy boyliklar va pul mablag‘lari inventarizatsiyasini o‘z vaqtida o‘tkazish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел бухгалтерии"))
async def buxgalteriya_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Buxgalteriya_ru.get_fullname()}\n\n"
                f"Должность    |    {Buxgalteriya_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Buxgalteriya_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Buxgalteriya_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Обеспечение организации бухгалтерского учета в соответствии с положением, утвержденным Министерством финансов Республики Узбекистан, контроль за эффективным использованием материальных, трудовых и финансовых ресурсов;\n\n"
             f"✅ Контролировать своевременный расчет и распределение заработной платы ППС, студенческих стипендий;\n\n"
             f"✅ Предоставлять полную и точную информацию о состоянии и движении активов, статусе имущественных прав и обязательств по счетам;\n\n"
             f"✅ Своевременная инвентаризация материальных ценностей и денежных средств;</i></b>"
    )


@dp.message_handler(Text(equals="Accounting Department"))
async def buxgalteriya_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Buxgalteriya_en.get_fullname()}\n\n"
                f"Position    |    {Buxgalteriya_en.get_position()}\n\n"
                f"Contact phone   |   {Buxgalteriya_en.get_number()}\n\n"
                f"Email address   |   {Buxgalteriya_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Ensuring the organization of accounting in accordance with the regulations approved by the Ministry of Finance of the Republic of Uzbekistan, control over the effective use of material, labor and financial resources;\n\n"
             f"✅ Control over the timely calculation and distribution of salaries of faculty and staff, student scholarships;\n\n"
             f"✅ Provide complete and accurate information on the status and movement of assets, the status of property rights and obligations in the accounts;\n\n"
             f"✅ Timely inventory of material assets and cash;</i></b>"
    )
