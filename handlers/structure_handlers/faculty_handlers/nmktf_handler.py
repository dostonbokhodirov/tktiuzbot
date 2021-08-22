from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_nmktf, ru_keyboard_nmktf, en_keyboard_nmktf
from loader import dp, bot


@dp.message_handler(Text(equals="Noorganik moddalar kimyoviy texnologiyasi fakulteti"))
async def nmktf_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultet to‘g‘risidagi ba'zi ma'lumotlar:</b>\n\n"
             f"<i>Fakultet sobiq ToshPIning kimyo-texnologiya fakulteti negizida <b>1991-yilda</b> tashkil etilgan.\n\n"
             f"Fakultet bitiruvchilari respublikamizning \n"
             f"    <b>- “O‘zkimyosanoat” DAK\n"
             f"    - “O‘zqurilishmateriallari” AK</b>\n"
             f"kabi sanoat korxonalarida mehnat qilmoqdalar...</i>",
        reply_markup=uz_keyboard_nmktf
    )


@dp.message_handler(Text(equals="Факультет химической технологии неорганических веществ"))
async def nmktf_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о факультете:</b>\n\n"
             f"<i>Факультет основан в <b>1991 году</b> на базе бывшего химико-технологического факультета ТашПИ.\n\n"
             f"Выпускники факультета работают на промышленных предприятиях республики, таких как \n"
             f"    <b>- ГАК «Узкимёсаноат»\n"
             f"    - АК «Узкурилишматериаллари».</b></i>",
        reply_markup=ru_keyboard_nmktf
    )


@dp.message_handler(Text(equals="Faculty of Chemical Technology of Inorganic Substances"))
async def nmktf_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the faculty:</b>\n\n"
             f"<i>The faculty was founded in <b>1991</b> on the basis of the former TashPI Faculty of Chemical Technology.\n\n"
             f"Graduates of the faculty work in industrial enterprises of the republic, such as \n"
             f"    <b>- SJSC “Uzkimyosanoat”\n"
             f"    - JSC “Uzqurilishmateriallari”.</b></i>",
        reply_markup=en_keyboard_nmktf
    )
