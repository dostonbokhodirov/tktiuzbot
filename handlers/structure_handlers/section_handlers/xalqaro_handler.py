import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Xalqaro_uz, Xalqaro_ru, Xalqaro_en

with open("pictures/xalqaro1.png", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Xalqaro aloqalar bo‘limi"))
async def xalqaro_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Xalqaro_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Xalqaro_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Xalqaro_uz.get_number()}\n\n"
                f"Email manzil   |   {Xalqaro_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Institutning xalqaro aloqalarini rivojlantirish;\n\n"
             f"✅ Xalqaro hamkorlik sohasida institut bo'limlarini muvofiqlashtirish;\n\n"
             f"✅ Xalqaro hamkorlik loyihalarini amalga oshirishda hujjatlarni rasmiylashtirishda ko’maklashish;\n\n"
             f"✅ Xalqaro hamkorlik sohasi bo’yicha ma’lumot va maslahat xizmatlarini ko'rsatish;\n\n"
             f"✅ Institut bo'limlari va tadbirlar o'rtasidagi yozishmalarni xorijiy tillar asosida qo'llab-quvvatlash;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел международные отношения"))
async def xalqaro_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Xalqaro_ru.get_fullname()}\n\n"
                f"Должность    |    {Xalqaro_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Xalqaro_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Xalqaro_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Развитие международных связей института;\n\n"
             f"✅ Координация работы подразделений института в области международного сотрудничества;\n\n"
             f"✅ Содействие в подготовке документов для реализации проектов международного сотрудничества;\n\n"
             f"✅ Оказание информационных и консультационных услуг в сфере международного сотрудничества;\n\n"
             f"✅ Сопровождение переписки между отделами института и мероприятиями на основе иностранных языков;</i></b>"
    )


@dp.message_handler(Text(equals="Department of International Relations"))
async def xalqaro_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Xalqaro_en.get_fullname()}\n\n"
                f"Position    |    {Xalqaro_en.get_position()}\n\n"
                f"Contact   |   {Xalqaro_en.get_number()}\n\n"
                f"Email address   |   {Xalqaro_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Development of international relations of the Institute;\n\n"
             f"✅ Coordination of departments of the institute in the field of international cooperation;\n\n"
             f"✅ Assistance in preparation of documents for the implementation of international cooperation projects;\n\n"
             f"✅ Providing information and consulting services in the field of international cooperation;\n\n"
             f"✅ Support of correspondence between departments of the institute and events on the basis of foreign languages;</i></b>"
    )
