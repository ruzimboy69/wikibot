import logging

import wikipedia
import requests
from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5418544586:AAE1w4XOhq4v2MFmykIqGJAMEgkSIXLGHoM'
# Configure logging
logging.basicConfig(level=logging.INFO)

wikipedia.set_lang("uz")
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalom aleykum bizning botimizga xush kelibsiz!!!")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + message.text)
        data = response.json()
        await message.answer(data[0]['meanings'][0]['definitions'][0]['definition'])
        translator = Translator()
        translated = translator.translate(data[0]['meanings'][0]['definitions'][0]['definition'], dest='uz')
        await message.answer("tarjimasi: "+translated.text)
        await message.answer_audio(data[0]['phonetics'][0]['audio'])
    except:
        await message.answer("topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
