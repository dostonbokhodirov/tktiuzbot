import asyncio

from aiogram import types
from aiogram.dispatcher.filters import Text

from keyboards import uz_keyboard_filial_sh, ru_keyboard_filial_sh, en_keyboard_filial_sh
from loader import dp, bot

with open("pictures/shahrisabz.jpg", "rb") as file:
    photo = file.read()


@dp.message_handler(Text(equals="TKTI Shahrisabz filiali"))
async def filial_sh_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Toshkent kimyo-texnologiya instituti Shahrisabz filiali\n\n"
                f"Ishonch telefoni    |    (75) 522-50-68\n\n"
                f"Email manzil   |   info@stict.uz\n\n"
                f"Manzil    |    <a href='https://bit.ly/tcti_filial'>Qashqadaryo viloyati, Shahrisabz shahri, Shahrisabz ko‘chasi, 20-uy</a>\n\n\n"
                f"Batafsil ma'lumotlarni quyidagi manzillar orqali ham olishingiz mumkin:\n\n"
                f"<a href='http://stict.uz'>Rasmiy sayt</a>    |    <a href='https://t.me/Shahrisabz_TKTI'>Telegram</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Filial haqida ba'zi ma'lumotlar:\n\n"
             f"<i>Qashqadaryo viloyatida oziq-ovqat mahsulotlari ishlab chiqarish sanoati salohiyatini yanada oshirish va iqtisodiyotning bazaviy tarmoqlarida oliy ma'lumotli kadrlar tayyorlashni kengaytirish maqsadida O‘zbekiston Respublikasi Oliy va o‘rta maxsus ta'lim vazirligi, Iqtisodiyot va sanoat vazirligi, Moliya vazirligi va Qashqadaryo viloyati hokimligining Qashqadaryo viloyatining Shahrisabz shahrida Toshkent kimyo-texnologiya institutining Shahrisabz filialini tashkil etish to‘g‘risidagi taklifiga rozilik berilgan.\n\n"
             f"Filialda o‘quv jarayoni 2019/2020-o‘quv yilidan boshlangan.</i></b>",
        reply_markup=uz_keyboard_filial_sh
    )


@dp.message_handler(Text(equals="ТКТИ Шахрисабзский филиал"))
async def filial_sh_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Шахрисабзский филиал Ташкентского химико-технологического института\n\n"
                f"Телефон доверия    |    (75) 522-50-68\n\n"
                f"Адрес электронной почты   |   info@stict.uz\n\n"
                f"Адрес    |    <a href='https://bit.ly/tcti_filial'>Кашкадарьинская область, город Шахрисабз, улица Шахрисабз, 20</a>\n\n\n"
                f"Вы также можете получить дополнительную информацию по следующим адресам:\n\n"
                f"<a href='http://stict.uz'>Официальный сайт</a>    |    <a href='https://t.me/Shahrisabz_TKTI'>Телеграм</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Немного информации о филиале:\n\n"
             f"<i>В целях дальнейшего увеличения потенциала пищевой промышленности Кашкадарьинской области и расширения подготовки кадров высшего образования в базовых отраслях экономики Министерство высшего и среднего специального образования, Министерство экономики и промышленности, Министерство финансов и Кашкадарьинская область Утверждено предложение о создании филиала Ташкентского химико-технологического института в г. Шахрисабз Кашкадарьинской области.\n\n"
             f"Учебный процесс в филиале стартовал в 2019/2020 учебном году.</i></b>",
        reply_markup=ru_keyboard_filial_sh
    )


@dp.message_handler(Text(equals="Shakhrisabz branch of TCTI"))
async def filial_sh_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=photo,
        caption=f"<b>Shakhrisabz branch of the Tashkent Chemical-Technological Institute\n\n"
                f"Helpline    |    (75) 522-50-68\n\n"
                f"Email address   |   info@stict.uz\n\n"
                f"Address    |    <a href='https://bit.ly/tcti_filial'>Kashkadarya region, Shakhrisabz city, Shakhrisabz street, 20</a>\n\n\n"
                f"You can also get more information at the following addresses:\n\n"
                f"<a href='http://stict.uz'>Official site</a>    |    <a href='https://t.me/Shahrisabz_TKTI'>Telegram</a></b>"
    )
    await asyncio.sleep(2)
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text=f"<b>Some information about the filial:\n\n"
             f"<i>In order to further increase the potential of the food industry in Kashkadarya region and expand the training of higher education in basic sectors of the economy, the Ministry of Higher and Secondary Special Education, the Ministry of Economy and Industry, the Ministry of Finance and the Kashkadarya region The proposal to establish a branch of the Tashkent Chemical-Technology Institute in Shakhrisabz, Kashkadarya region, was approved.\n\n"
             f"The training process at the filial started in the 2019/2020 academic year.</i></b>",
        reply_markup=en_keyboard_filial_sh
    )
