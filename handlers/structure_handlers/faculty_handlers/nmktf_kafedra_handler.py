from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Noorganik moddalar kimyoviy texnologiyasi fakulteti kafedralari"))
async def nmktf_kafedra_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultetda quyidagi kafedralar mavjud:\n\n"
             f"<i>1. Silikat materiallari texnologiyasi\n"
             f"2. Analitik, fizik va kolloid kimyo\n"
             f"3. Noorganik moddalar texnologiyasi\n"
             f"4. Texnologik jarayon va qurilmalar\n"
             f"5. Sanoat ekologiyasi\n"
             f"6. Umumiy va noorganik kimyo</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры факультета химической технологии неорганических веществ"))
async def nmktf_kafedra_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>На факультете действуют следующие кафедры:\n\n"
             f"<i>1. Технология силикатных материалов\n"
             f"2. Аналитическая, физическая и коллоидная химия\n"
             f"3. Технология неорганических веществ\n"
             f"4. Технологические процессы и устройства\n"
             f"5. Промышленная экология\n"
             f"6. Общая и неорганическая химия</i></b>"
    )


@dp.message_handler(Text(equals="Departments of the Faculty of Chemical Technology of Inorganic Substances"))
async def nmktf_kafedra_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The faculty has the following departments:\n\n"
             f"<i>1. Technology of silicate materials\n"
             f"2. Analytical, physical and colloid chemistry\n"
             f"3. Technology of inorganic substances\n"
             f"4. Technological processes and devices\n"
             f"5. Industrial ecology\n"
             f"6. General and inorganic chemistry</i></b>"
    )
