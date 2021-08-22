import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from Class import Magistratura_uz, Magistratura_ru, Magistratura_en

with open("pictures/magistratura.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Magistratura bo‘limi"))
async def magistratura_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Magistratura_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Magistratura_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Magistratura_uz.get_number()}\n\n"
                f"Email manzil   |   {Magistratura_uz.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Bo‘limning asosiy vazifalari:\n\n"
             f"<i>✅ Magistrlar tayyorlash bo‘yicha o‘quv jarayonini tashkil etish, ta’lim va o‘qitish sifatini nazorat qilish;\n\n"
             f"✅ Magistratura faoliyatini boshqarish, ta’lim jarayonlarini tashkil etishning shakli va mexanizmlarini modernizasiya qilish;\n\n"
             f"✅ Magistratura mutaxassisliklarini zaruriy darsliklar va adabiyotlar bilan ta’minlashni tashkil etish, bu ishga yetuk olimlar, yuqori malakali mutaxassislarni jalb etish, ilmiy sohani rivojlantirish;\n\n"
             f"✅ Magistratura talabalari tomonidan o‘quv-izlanish va ilmiy-tadqiqot ishlari amalga oshirilishini nazorat qilish;\n\n"
             f"✅ Kafedralarning magistrlar tayyorlash bo‘yicha faoliyatini muvofiqlashtirish va nazorat qilish;</i></b>"
    )


@dp.message_handler(Text(equals="Отдел магистратуры"))
async def magistratura_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Magistratura_ru.get_fullname()}\n\n"
                f"Должность    |    {Magistratura_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Magistratura_ru.get_number()}\n\n"
                f"Адрес электронной почты   |   {Magistratura_ru.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Основные задачи отдела:\n\n"
             f"<i>✅ Организация процесса обучения в магистратуре, контроль качества обучения и подготовки кадров;\n\n"
             f"✅ Управление магистерской деятельностью, модернизация форм и механизмов организации образовательных процессов;\n\n"
             f"✅ Организация обеспечения магистерских специальностей необходимыми учебниками и литературой, привлечение к этой работе ведущих ученых, высококвалифицированных специалистов, развитие научного направления;\n\n"
             f"✅ Контролировать выполнение аспирантами научно-исследовательских и опытно-конструкторских работ;\n\n"
             f"✅ Координация и курирование деятельности отделов по подготовке магистров;</i></b>"
    )


@dp.message_handler(Text(equals="Department of Magistracy"))
async def magistratura_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Magistratura_en.get_fullname()}\n\n"
                f"Position    |    {Magistratura_en.get_position()}\n\n"
                f"Contact phone   |   {Magistratura_en.get_number()}\n\n"
                f"Email address   |   {Magistratura_en.get_email()}</b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The main tasks of the department:\n\n"
             f"<i>✅ Organization of the educational process for master's degree, quality control of education and training;\n\n"
             f"✅ Management of master's activities, modernization of forms and mechanisms of organization of educational processes;\n\n"
             f"✅ Organize the provision of master's specialties with the necessary textbooks and literature, the involvement of leading scientists, highly qualified specialists in this work, the development of the scientific field;\n\n"
             f"✅ Supervise the implementation of research and development work by graduate students;\n\n"
             f"✅ Coordinating and supervising the activities of departments for the preparation of masters;</i></b>"
    )
