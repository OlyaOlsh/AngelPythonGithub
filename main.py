import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiohttp.web_app import Application
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import WebAppData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# импорты
from config_reader import config



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
# bot = Bot(token="7048234624:AAENz12gQRWEQDWaeS_VhnUg7wiXCuKkK2Q")

# Для записей с типом Secret* необходимо
# вызывать метод get_secret_value(),
# чтобы получить настоящее содержимое вместо '*******'
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
#@dp.message_handler(Command("start"))
#async def cmd_start(message: types.Message):
#    await message.answer("Hello!")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем кнопку для запуска Web App
    web_app_button = InlineKeyboardButton(
        text="Запустить Web App",
        web_app=WebAppInfo(url="https://olyaolsh.github.io/angelBot.gethub.io/")  # URL вашего веб-приложения
    )

    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[web_app_button]])

    # Отправляем сообщение с клавиатурой
    await message.answer("Нажмите кнопку, чтобы запустить веб-приложение:", reply_markup=keyboard)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎲")

if __name__ == '__main__':
    asyncio.run(main())

