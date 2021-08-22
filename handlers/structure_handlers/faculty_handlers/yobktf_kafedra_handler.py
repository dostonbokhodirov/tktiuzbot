from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Yoqilg‘i va organik birikmalar kimyoviy texnologiyasi fakulteti kafedralari"))
async def yobktf_kafedra_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultetda quyidagi kafedralar mavjud:\n\n"
             f"<i>1. Yuqori molekulali birikmalar va plastmassalar texnologiyasi\n"
             f"2. Organik kimyo va asosiy organik sintez texnologiyasi\n"
             f"3. Neft va gazni qayta ishlash kimyoviy texnologiyasi\n"
             f"4. Selluloza va yog‘ochsozlik texnologiyasi\n"
             f"5. Fizika va elektrotexnika</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры химической технологии топлив и органических соединений"))
async def yobktf_kafedra_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>На факультете действуют следующие кафедры:\n\n"
             f"<i>1. Технология высокомолекулярных соединений и пластиков\n"
             f"2. Органическая химия и технология основного органического синтеза\n"
             f"3. Химическая технология переработки нефти и газа\n"
             f"4. Целлюлоза и технология обработки древесины\n"
             f"5. Физика и электротехника</i></b>"
    )


@dp.message_handler(Text(equals="Departments of the Faculty of Chemical Technology of Fuels and Organic Compounds"))
async def yobktf_kafedra_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The faculty has the following departments:\n\n"
             f"<i>1. Technology of high molecular weight compounds and plastics\n"
             f"2. Organic chemistry and basic organic synthesis technology\n"
             f"3. Chemical technology of oil and gas refining\n"
             f"4. Cellulose and woodworking technology\n"
             f"5. Physics and electrical engineering</i></b>"
    )
