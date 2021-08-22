from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_yobktf, ru_keyboard_yobktf, en_keyboard_yobktf
from loader import dp, bot


@dp.message_handler(Text(equals="Yoqilg‘i va organik birikmalar kimyoviy texnologiyasi fakulteti"))
async def yobktf_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultet to‘g‘risidagi ba'zi ma'lumotlar:</b>\n\n"
             f"<i>Fakultet dastlab TKTI tarkibida <b>1991-yili “Organik moddalar ishlab chiqarish texnologiyasi”</b> fakulteti nomi bilan tashkil etilgan.\n\n"
             f"Fakultet bitiruvchilari respublikamizning \n"
             f"    <b>- “O‘zkimyosanoat” DAK\n"
             f"    - “O‘zneftgaz” MXK\n"
             f"    - Yog'och va mebel ishlab chiqarish</b>\n"
             f"kabi sanoat korxonalarida mehnat qilmoqdalar...</i>",
        reply_markup=uz_keyboard_yobktf
    )


@dp.message_handler(Text(equals="Факультет химической технологии топлива и органических соединений"))
async def yobktf_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о факультете:</b>\n\n"
             f"<i>Факультет впервые был создан в <b>1991 году</b> в составе ТКТИ под названием <b>«Технология производства органических веществ»</b>.\n\n"
             f"Выпускники факультета работают на таких промышленных предприятиях, как \n"
             f"    <b>- «Узкимёсаноат» АО\n"
             f"    - «Узнефтегаз» НХК\n"
             f"    - Деревообрабатывающие и мебельные фабрики</b>.</i>",
        reply_markup=ru_keyboard_yobktf
    )


@dp.message_handler(Text(equals="Faculty of Chemical Technology of Fuels and Organic Compounds"))
async def yobktf_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the faculty:</b>\n\n"
             f"<i>The faculty was first established <b>in 1991</b> as a part of TCTI under the name <b>“Technology of production of organic substances”</b>.\n\n"
             f"Graduates of the faculty work in such industrial enterprises as \n"
             f"    <b>- “Uzkimyosanoat” JSC\n"
             f"    - “UzneftEgaz” NHK\n"
             f"    - Wood and furniture factories</b>.</i>",
        reply_markup=en_keyboard_yobktf
    )
