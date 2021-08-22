from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_mktf, ru_keyboard_mktf, en_keyboard_mktf
from loader import dp, bot


@dp.message_handler(Text(equals="Menejment va kasb ta'limi fakulteti"))
async def mktf_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultet to‘g‘risidagi ba'zi ma'lumotlar:</b>\n\n"
             f"<i>Fakultet <b>2001-yilda</b> TKTIning ilmiy kengashi qarori bilan tashkil etilgan. 2002-yilda <b>“Menejment va axborot texnologiyasi”</b> nomini olgan.\n"
             f"2004-yilda TKTIning ilmiy kengashi qarori bilan <b>“Menejment va kasb ta'limi”</b> deb nomlangan.\n\n"
             f"Fakultet tarkibida 5ta kafedra va 1ta sikl bo‘lib, shulardan 3tasi mutaxassislik kafedrasi hisoblanadi...</i>",
        reply_markup=uz_keyboard_mktf
    )


@dp.message_handler(Text(equals="Факультет менеджмента и профессионального образования"))
async def mktf_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о факультете:</b>\n\n"
             f"<i>Факультет создан в <b>2001 году</b> решением Ученого совета ТКТИ. В 2002 году он был переименован в <b>«Менеджмент и информационные технологии»</b>.\n"
             f"В 2004 году решением Ученого совета ТКТИ он был переименован в <b>«Менеджмент и профессиональное образование»</b>.\n\n"
             f"Факультет состоит из 5 кафедр и 1 цикла, 3 из которых являются специализированными кафедрами...</i>",
        reply_markup=ru_keyboard_mktf
    )


@dp.message_handler(Text(equals="Faculty of Management and Vocational Education"))
async def mktf_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the faculty:</b>\n\n"
             f"<i>The faculty was founded in <b>2001</b> by the decision of the Student Council TCTI. In 2002 it was renamed <b>“Management and Information Technology”</b>.\n"
             f"In 2004, by the decision of the Academic Council of TCTI, it was renamed <b>“Management and Vocational Education”</b>.\n\n"
             f"The faculty consists of 5 departments and 1 cycle, 3 of which are specialty departments ...</i>",
        reply_markup=en_keyboard_mktf
    )
