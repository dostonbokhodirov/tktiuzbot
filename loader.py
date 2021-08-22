import sqlite3

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

connect = sqlite3.connect("data.db")
cursor = connect.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
   user_id INT PRIMARY KEY,
   fullname TEXT,
   username TEXT,
   language TEXT); 
""")
connect.commit()
