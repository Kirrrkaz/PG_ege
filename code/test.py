from aiogram import Bot, Dispatcher, executor, types
import logging

from config import API_TOKEN


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    photo = open("1.jpg", "rb") # rb - чтение байтов, wb - запись байтов.
    await bot.send_photo(message.chat.id, photo)




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) 