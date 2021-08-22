from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="Kafedralar"))
async def department_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Institutda quyidagi kafedralar mavjud:\n\n"
             f"<i>✅ Fizika va elektrotexnika kafedrasi\n"
             f"✅ Ijtimoiy-siyosiy fanlar kafedrasi\n"
             f"✅ Jismoniy tarbiya va sport kafedrasi\n"
             f"✅ Biotexnologiya kafedrasi\n"
             f"✅ Informatika, avtomatlashtirish va boshqaruv kafedrasi\n"
             f"✅ Oziq-ovqat sanoati mashina va jihozlari-mexanika asoslari kafedrasi\n"
             f"✅ Go‘sht-sut va konserva mahsulotlar texnologiyasi kafedrasi\n"
             f"✅ Oziq-ovqat mahsulotlari texnologiyasi kafedrasi\n"
             f"✅ Organik kimyo va og‘ir organik sintez texnologiyasi kafedrasi\n"
             f"✅ Selluloza va yog‘ochsozlik texnologiyasi kafedrasi\n"
             f"✅ Yuqori molekulali birikmalar va plastmassalar kafedrasi\n"
             f"✅ Neft gazni qayta ishlash kimyoviy texnologiyasi kafedrasi\n"
             f"✅ Oliy matematika kafedrasi\n"
             f"✅ Silikat materiallar, nodir va kamyob metallar texnologiyasi kafedrasi\n"
             f"✅ Analitik, fizikaviy va kolloid kimyo kafedrasi\n"
             f"✅ Noorganik moddalar kimyoviy texnologiyasi kafedrasi\n"
             f"✅ Kimyoviy texnologik jarayon va qurilmalar kafedrasi\n"
             f"✅ Sanoat ekologiyasi kafedrasi\n"
             f"✅ Umumiy va noorganik kimyo kafedrasi\n"
             f"✅ Sаnоаt iqtisоdiyoti vа mеnеjmеnti kаfеdrаsi\n"
             f"✅ Mahsulot sifati menejmenti kafedrasi\n"
             f"✅ Kasb ta'limi kafedrasi\n"
             f"✅ Tillar kafedrasi\n"
             f"✅ Xorijiy tillar kafedrasi\n"
             f"✅ Enologiya va umumiy ovqatlanishni tashkil etish kafedrasi</i></b>"
    )


@dp.message_handler(Text(equals="Кафедры"))
async def department_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>В институте действуют следующие кафедры:\n\n"
             f"<i>✅ Кафедра физики и электротехники\n"
             f"✅ Кафедра социальных и политических наук\n"
             f"✅ Кафедра физической культуры и спорта\n"
             f"✅ Кафедра биотехнологии\n"
             f"✅ Кафедра информатики, автоматизации и управления\n"
             f"✅ Кафедра механических основ машин и оборудования пищевой промышленности\n"
             f"✅ Кафедра мясомолочной технологии\n"
             f"✅ Кафедра пищевых технологий\n"
             f"✅ Кафедра органической химии и технологии тяжелого органического синтеза\n"
             f"✅ Кафедра технологии целлюлозы и древесины\n"
             f"✅ Кафедра высокомолекулярных соединений и пластиков\n"
             f"✅ Кафедра химической технологии переработки нефти и газа\n"
             f"✅ Кафедра высшей математики\n"
             f"✅ Кафедра силикатных материалов, технологии редких и редких металлов\n"
             f"✅ Кафедра аналитической, физической и коллоидной химии\n"
             f"✅ Кафедра химической технологии неорганических веществ\n"
             f"✅ Кафедра химико-технологических процессов и аппаратов\n"
             f"✅ Кафедра промышленной экологии\n"
             f"✅ Кафедра общей и неорганической химии\n"
             f"✅ Кафедра экономики и менеджмента промышленности\n"
             f"✅ Кафедра управления качеством продукции\n"
             f"✅ Кафедра профессионального образования\n"
             f"✅ Кафедра языков\n"
             f"✅ Кафедра иностранных языков\n"
             f"✅ Кафедра энологии и общественного питания</i></b>"
    )


@dp.message_handler(Text(equals="Chairs"))
async def department_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>The institute has the following departments:\n\n"
             f"<i>✅ Department of Physics and Electrical Engineering\n"
             f"✅ Department of Social and Political Sciences\n"
             f"✅ Department of Physical Culture and Sports\n"
             f"✅ Department of Biotechnology\n"
             f"✅ Department of Informatics, Automation and Management\n"
             f"✅ Department of Mechanical Fundamentals of Machinery and Equipment of the Food Industry\n"
             f"✅ Department of Meat and Dairy Technology\n"
             f"✅ Department of Food Technology\n"
             f"✅ Department of Organic Chemistry and Heavy Organic Synthesis Technology\n"
             f"✅ Department of Pulp and Wood Technology\n"
             f"✅ Department of High Molecular Compounds and Plastics\n"
             f"✅ Department of Chemical Technology of Oil and Gas Processing\n"
             f"✅ Department of Higher Mathematics\n"
             f"✅ Department of Silicate Materials, Rare and Rare Metals Technology\n"
             f"✅ Department of Analytical, Physical and Colloid Chemistry\n"
             f"✅ Department of Chemical Technology of Inorganic Substances\n"
             f"✅ Department of Chemical Technological Processes and Devices\n"
             f"✅ Department of Industrial Ecology\n"
             f"✅ Department of General and Inorganic Chemistry\n"
             f"✅ Department of Industrial Economics and Management\n"
             f"✅ Department of Product Quality Management\n"
             f"✅ Department of Vocational Education\n"
             f"✅ Department of Languages\n"
             f"✅ Department of Foreign Languages\n"
             f"✅ Department of Enology and Catering</i></b>"
    )
