from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Vinochilik texnologiyasi va sanoat uzumchiligi fakulteti kafedralari"))
async def vtsuf_kafedra_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultetda quyidagi kafedralar mavjud:\n\n"
             f"<i>1. Biotexnologiya\n"
             f"2. Enologiya\n"
             f"3. Bijg‘ish mahsulotlari va alkogolsiz ichimliklar texnologiyasi</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры факультета технологии вина и промышленного виноградарства"))
async def vtsuf_kafedra_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>На факультете действуют следующие кафедры:\n\n"
             f"<i>1. Биотехнология\n"
             f"2. Энология\n"
             f"3. Технология выпечки и безалкогольных напитков</i></b>"
    )


@dp.message_handler(Text(equals="Departments of the Faculty of Wine Technology and Industrial Viticulture"))
async def vtsuf_kafedra_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The faculty has the following departments:\n\n"
             f"<i>1. Biotechnology\n"
             f"2. Enology\n"
             f"3. Baking and non-alcoholic beverage technology</i></b>"
    )
