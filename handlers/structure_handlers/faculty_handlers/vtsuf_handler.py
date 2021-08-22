from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_vtsuf, ru_keyboard_vtsuf, en_keyboard_vtsuf
from loader import dp, bot


@dp.message_handler(Text(equals="Vinochilik texnologiyasi va sanoat uzumchiligi fakulteti"))
async def vtsuf_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultet to‘g‘risidagi ba'zi ma'lumotlar:</b>\n\n"
             f"<i>Fakultet <b>2018-yilda</b> TKTI rektori buyrug‘i asosida tashkil etilgan.\n"
             f"Fakultet tarkibida 3ta kafedra mavjud.\n\n"
             f"Fakultet <b>“O‘zsharobsanoat” AJ</b> tasarrufidagi barcha ishlab chiqarish korxonalari bilan hamkorlik qilib kelmoqda...</i>",
        reply_markup=uz_keyboard_vtsuf
    )


@dp.message_handler(Text(equals="Факультет технологии вина и промышленного виноградарства"))
async def vtsuf_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о факультете:</b>\n\n"
             f"<i>Факультет создан в <b>2018 году</b> приказом ректора ТКТИ.\n"
             f"Факультет состоит из 3-х кафедр.\n\n"
             f"Факультет сотрудничает со всеми производственными предприятиями <b>АК «Узшаробсаноат»</b>...</i>",
        reply_markup=ru_keyboard_vtsuf
    )


@dp.message_handler(Text(equals="Faculty of Wine Technology and Industrial Viticulture"))
async def vtsuf_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the faculty:</b>\n\n"
             f"<i>The faculty was established <b>in 2018</b> by the order of the rector of TCTI.\n"
             f"The faculty consists of 3 departments.\n\n"
             f"The faculty cooperates with all production enterprises of <b>JSC “Uzsharobsanoat”</b>...</i>",
        reply_markup=en_keyboard_vtsuf
    )
