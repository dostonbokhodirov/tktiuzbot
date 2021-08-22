from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot
# from Class import Prorector_yoshlar_uz, Prorector_yoshlar_ru, Prorector_yoshlar_en

with open("pictures/man.png", "rb") as file:
    photo = file.read()


# @dp.message_handler(Text(equals="Yoshlar bilan ishlash bo‘yicha prorektor"))
# async def prorector_yoshlar_uz(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#     await bot.send_photo(
#         chat_id=message.chat.id,
#         photo=photo,
#         caption=f"<b>{Prorector_yoshlar_uz.get_fullname()}\n\n"
#                 f"Lavozim    |    {Prorector_yoshlar_uz.get_position()}\n\n"
#                 f"Murojaat uchun telefon   |   {Prorector_yoshlar_uz.get_number()}\n\n"
#                 f"Email manzil   |   {Prorector_yoshlar_uz.get_email()}\n\n"
#                 f"Qabul vaqti   |   {Prorector_yoshlar_uz.get_reception()}</b>"
#     )
#
#
# @dp.message_handler(Text(equals="Проректор по делам молодежи"))
# async def prorector_yoshlar_ru(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#     await bot.send_photo(
#         chat_id=message.chat.id,
#         photo=photo,
#         caption=f"<b>{Prorector_yoshlar_ru.get_fullname()}\n\n"
#                 f"Должность    |    {Prorector_yoshlar_ru.get_position()}\n\n"
#                 f"Контактный телефон   |   {Prorector_yoshlar_ru.get_number()}\n\n"
#                 f"Адрес электронной почты   |   {Prorector_yoshlar_ru.get_email()}\n\n"
#                 f"Время приема   |   {Prorector_yoshlar_ru.get_reception()}</b>"
#     )
#
#
# @dp.message_handler(Text(equals="Vice Rector for Youth Affairs"))
# async def prorector_yoshlar_en(message: types.Message):
#     await bot.send_chat_action(message.chat.id, "typing")
#     await bot.send_photo(
#         chat_id=message.chat.id,
#         photo=photo,
#         caption=f"<b>{Prorector_yoshlar_en.get_fullname()}\n\n"
#                 f"Position    |    {Prorector_yoshlar_en.get_position()}\n\n"
#                 f"Contact phone   |   {Prorector_yoshlar_en.get_number()}\n\n"
#                 f"Email address   |   {Prorector_yoshlar_en.get_email()}\n\n"
#                 f"Reception time   |   {Prorector_yoshlar_en.get_reception()}</b>"
#     )


@dp.message_handler(Text(equals="Yoshlar bilan ishlash bo‘yicha prorektor"))
async def prorector_yoshlar_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Hozirda bu vakant lavozim!</b>"
    )


@dp.message_handler(Text(equals="Проректор по делам молодежи"))
async def prorector_yoshlar_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Сейчас это вакансия!</b>"
    )


@dp.message_handler(Text(equals="Vice Rector for Youth Affairs"))
async def prorector_yoshlar_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>This is a vacancy now!</b>"
    )
