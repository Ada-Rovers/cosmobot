import asyncio
import os
import logging
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не найден! Убедись, что переменная окружения установлена.")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_handler(message: Message):
    logger.info(f"✅ Пользователь {message.from_user.id} начал сессию.")
    await message.answer("🌟 Привет! Я — КосмоБот. Хочешь предсказание? Напиши /predict")

@dp.message(commands=["predict"])
async def predict_handler(message: Message):
    predictions = [
        "✨ Сегодня тебе обязательно повезёт!",
        "🚀 Время начинать новое!",
        "🌌 Вселенная готовит тебе сюрприз.",
        "🌠 Ты — магнит для удачи сегодня.",
        "🪐 Всё получится, если веришь в себя!"
    ]
    prediction = random.choice(predictions)
    logger.info(f"🔮 Предсказание для {message.from_user.id}: {prediction}")
    await message.answer(prediction)

async def main():
    logger.info("🚀 Бот запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.exception(f"🔥 Ошибка при запуске: {e}")
