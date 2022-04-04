from json import load
from aiogram import Bot, Dispatcher, executor, types
import logging

from config import API_TOKEN
import keyboard as kb

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# start

@dp.message_handler(commands=["start"])
async def manual(msg: types.Message):
    with open("1.json", "r") as f:
        sys = load(f)
    await msg.answer(f"""Приветсвтую, {msg.from_user.first_name} 👋\nЯ - бот {sys['name']} 🤖, проверяю ваши знания по производной.\n
    📂 Выберите уровень сложности:""", reply_markup=kb.mainMenu )



# создать директорию с пикчами
# забить варики с ответами + проверку
# NON MORE IDEAS ?? ??

@dp.callback_query_handler(text_contains="button_easy")
async def ans(call: types.CallbackQuery):
   await bot.delete_message(call.from_user.id, call.message.message_id)

   if call.data == "button_easy":
       photo = open("derivative\e_task_1.png", "rb")
       await bot.send_photo(call.from_user.id, photo)
       await bot.send_message(call.from_user.id, "Выберите вариант ответа:", reply_markup=kb.ans1)

    
@dp.message_handler(regexp='(^производная)')
async def cats(message: types.Message):
    with open('code\derivative\pic1.png', 'rb') as photo:
        await message.reply_photo(photo, caption='Варианты ответов: ')     





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)