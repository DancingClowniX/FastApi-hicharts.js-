from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

BOT_TOKEN = '6914265431:AAH8S7EuRJ8YS7AE-bjJ72YQeuYCOz837Zw'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


geo_btn: KeyboardButton = KeyboardButton(
    text="Заказать геолокацию",
    request_location=True
)

keyboard = ReplyKeyboardMarkup(keyboard=[[geo_btn]], resize_keyboard=True)


@dp.message(Command(commands="button"))
async def cmd_start(message: Message):
    await message.answer(
        text='Клавиатура вот такая',
        reply_markup=keyboard
    )

if __name__ == '__main__':
    dp.run_polling(bot)