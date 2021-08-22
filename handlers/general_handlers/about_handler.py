from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp, bot


@dp.message_handler(Text(equals="📋 Institut haqida"))
async def about_uz(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text="https://telegra.ph/Toshkent-kimyo-texnologiya-instituti-haqida-06-28"
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_video(
        chat_id=message.chat.id,
        video="https://t.me/TKTI_Official/16147",
        caption=f"<b>Bu video orqali Toshkent kimyo-texnologiya instituti haqida batafsil ma'lumot olishingiz mumkin.</b>"
    )


@dp.message_handler(Text(equals="📋 Об институте"))
async def about_ru(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text="https://telegra.ph/O-Tashkentskom-himiko-tehnologicheskom-institute-07-22"
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_video(
        chat_id=message.chat.id,
        video="https://t.me/TKTI_Official/16147",
        caption=f"<b>Из этого видео вы можете узнать больше о Ташкентском химико-технологическом институте.\n"
                f"Но это видео на узбекском языке. Приносим извинения за доставленные неудобства.</b>"
    )


@dp.message_handler(Text(equals="📋 About the institute"))
async def about_en(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    await message.answer(
        text="https://telegra.ph/About-Tashkent-Chemical-Technological-Institute-07-23"
    )
    await bot.send_chat_action(message.chat.id, "typing")
    await bot.send_video(
        chat_id=message.chat.id,
        video="https://t.me/TKTI_Official/16147",
        caption=f"<b>In this video you can learn more about the Tashkent Chemical-Technological Institute.\n"
                f"But this video is in Uzbek. Sorry for the inconvenience.</b>"
    )
