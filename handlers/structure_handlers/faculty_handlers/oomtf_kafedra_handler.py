from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Oziq-ovqat mahsulotlari texnologiyasi fakulteti kafedralari"))
async def oomtf_kafedra_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultetda quyidagi kafedralar mavjud:\n\n"
             f"<i>1. Oziq-ovqat mahsulotlari texnologiyasi\n"
             f"2. Informatika, avtomatlashtirish va boshqaruv\n"
             f"3. Oziq-ovqat sanoati mashina va jihozlari-mexanika asoslari\n"
             f"4. Oziq-ovqat xavfsizligi</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры факультета пищевых технологий"))
async def oomtf_kafedra_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>На факультете действуют следующие кафедры:\n\n"
             f"<i>1. Пищевые технологии\n"
             f"2. Информатика, автоматизация и управление\n"
             f"3. Основы машиностроения и оборудования пищевой промышленности\n"
             f"4. Продовольственная безопасность</i></b>"
    )


@dp.message_handler(Text(equals="Departments of the Faculty of Food Technology"))
async def oomtf_kafedra_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The faculty has the following departments:\n\n"
             f"<i>1. Food technology\n"
             f"2. Informatics, automation and management\n"
             f"3. Basics of machinery and equipment-mechanics of the food industry\n"
             f"4. Food security</i></b>"
    )
