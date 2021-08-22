from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_oomtf, ru_keyboard_oomtf, en_keyboard_oomtf
from loader import dp, bot


@dp.message_handler(Text(equals="Oziq-ovqat mahsulotlari texnologiyasi fakulteti"))
async def oomtf_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultet to‘g‘risidagi ba'zi ma'lumotlar:</b>\n\n"
             f"<i>Oziq-ovqat mahsulotlari texnologiyasi bo‘yicha muxandis kadrlar tayyorlash dastlab <b>1940-yilda</b> SazPI tarkibida amalga oshirilgan.\n\n"
             f"Fakultet bitiruvchilari respublikamizning \n"
             f"    <b>- “O‘zdonmahsulot” DAK\n"
             f"    - “O‘zkimyosanoat” AK\n"
             f"    - “O‘zpaxta-yog‘” AJ\n"
             f"    - “O’zbekoziq-ovqat” AJ</b>\n"
             f"kabi sanoat korxonalarida mehnat qilmoqdalar...</i>",
        reply_markup=uz_keyboard_oomtf
    )


@dp.message_handler(Text(equals="Факультет пищевых технологий"))
async def oomtf_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о факультете:</b>\n\n"
             f"<i>Подготовка инженеров пищевых технологий впервые была проведена в <b>1940 году</b> в рамках СазПИ.\n\n"
             f"Выпускники факультета работают на таких промышленных предприятиях республики, как \n"
             f"    <b>- ГАО «Уздонмахсулот»\n"
             f"    - АО «Узкимёсаноат\n"
             f"    - АО «Узпахта-Йог»\n"
             f"    - АО «Узбекозик-овкат».</b></i>",
        reply_markup=ru_keyboard_oomtf
    )


@dp.message_handler(Text(equals="Faculty of Food Technology"))
async def oomtf_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the faculty:</b>\n\n"
             f"<i>The training of food technology engineers was first carried out <b>in 1940</b> as part of SazPI.\n\n"
             f"Graduates of the faculty work in such industrial enterprises of the Republic as \n"
             f"    <b>- “Uzdonmakhsulot” SJSC\n"
             f"    - “Uzkimyosanoat” JSC\n"
             f"    - “Uzpakhta-Yog” JSC\n"
             f"    - “Uzbekoziq-ovqat” JSC</b>.</i>",
        reply_markup=en_keyboard_oomtf
    )
