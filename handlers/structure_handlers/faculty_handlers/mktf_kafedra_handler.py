from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Menejment va kasb ta'limi fakulteti kafedralari"))
async def mktf_kafedra_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Fakultetda quyidagi kafedralar mavjud:\n\n"
             f"<i>1. Sanoat iqtisodiyoti va menejmenti\n"
             f"2. Mahsulot sifati menejmenti\n"
             f"3. Kasb ta'limi\n"
             f"4. Tillar\n"
             f"5. Oliy matematika</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры факультета менеджмента и профессионального образования"))
async def mktf_kafedra_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>На факультете действуют следующие кафедры:\n\n"
             f"<i>1. Промышленная экономика и менеджмент\n"
             f"2. Управление качеством продукции\n"
             f"3. Профессионально-техническое образование\n"
             f"4. Языки\n"
             f"5. Высшая математика</i></b>"
    )


@dp.message_handler(Text(equals="Departments of the Faculty of Management and Vocational Education"))
async def mktf_kafedra_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The faculty has the following departments:\n\n"
             f"<i>1. Industrial economics and management\n"
             f"2. Product quality management\n"
             f"3. Vocational education\n"
             f"4. Languages\n"
             f"5. Higher mathematics</i></b>"
    )
