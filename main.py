from aiogram import Bot, Dispatcher, executor, types
import config
import random

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
count = 0

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello, i\'m echo bot')

@dp.message_handler(commands=['discription'])
async def start_command(message: types.Message):
    await message.answer(config.DISCRIPT_INFO)

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(config.HELP_INFO)

@dp.message_handler(commands=['count'])
async def start_command(message: types.Message):
    global count
    await message.answer(count)
    count += 1

@dp.message_handler()
async def start_command(message: types.Message):
    mess = message.text
    if '0' in mess:
        await message.answer('YES')
    else:
        await message.answer('NO')
    
def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
