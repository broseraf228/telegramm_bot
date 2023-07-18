from aiogram import Bot, Dispatcher, executor, types
import config


bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Hello, i\'m echo bot')

@dp.message_handler(commands=['discription'])
async def start_command(message: types.Message):
    await message.answer(config.DISCRIPT_INFO)

@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(config.HELP_INFO)

@dp.message_handler()
async def start_command(message: types.Message):
    mess = message.text
    if len(mess.split()) < 3:
        await message.answer(mess.upper())
    
def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
