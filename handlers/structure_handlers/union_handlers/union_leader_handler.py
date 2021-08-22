from aiogram import types
from aiogram.dispatcher.filters import Text


from loader import dp, bot
from Class import Union_uz, Union_ru, Union_en

with open("pictures/union.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="Yoshlar Ittifoqi yetakchisi"))
async def union_leader_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Union_uz.get_fullname()}\n\n"
                f"Lavozim    |    {Union_uz.get_position()}\n\n"
                f"Murojaat uchun telefon   |   {Union_uz.get_number()}\n\n"
                f"Telegram   |   {Union_uz.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Лидер Союза молодежи"))
async def union_leader_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Union_ru.get_fullname()}\n\n"
                f"Должность    |    {Union_ru.get_position()}\n\n"
                f"Контактный телефон   |   {Union_ru.get_number()}\n\n"
                f"Телеграм   |   {Union_ru.get_email()}</b>"
    )


@dp.message_handler(Text(equals="Leader of the Youth Union"))
async def union_leader_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>{Union_en.get_fullname()}\n\n"
                f"Position    |    {Union_en.get_position()}\n\n"
                f"Contact phone   |   {Union_en.get_number()}\n\n"
                f"Telegram   |   {Union_en.get_email()}</b>"
    )
