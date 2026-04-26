import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes


TOKEN = (8216472814:AAEdb-q43nxbPVEG879z-YpTphfz2KRjQ2o)

bot = Bot(8216472814:AAEdb-q43nxbPVEG879z-YpTphfz2KRjQ2o)

print("BOT STARTED")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text("Ты написал: " + text)

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle))

print("Bot started")
app.run_polling()user_memory = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    text = update.message.text

    if user_id not in user_memory:
        user_memory[user_id] = [
            {
                "role": "system",
                "content": (
                    "Ты очень точный AI помощник. "
                    "Отвечай быстро, чётко и без лишней воды. "
                    "Если вопрос по математике — ОБЯЗАТЕЛЬНО: "
                    "1) покажи формулу "
                    "2) реши шаг за шагом "
                    "3) дай 1-2 похожих примера с ответами."
                )
            }
        ]

    user_memory[user_id].append({"role": "user", "content": text})

    try:
        response = ollama.chat(
            model="llama3:8b",
            messages=user_memory[user_id],
            options={
                "temperature": 0.3,   # точнее ответы
                "num_predict": 300    # быстрее (ограничение длины)
            }
        )

        answer = response["message"]["content"]

        user_memory[user_id].append({"role": "assistant", "content": answer})

        # ограничиваем память
        if len(user_memory[user_id]) > 10:
            user_memory[user_id] = user_memory[user_id][-10:]

        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("⚡ Быстрый AI бот запущен...")
app.run_polling()