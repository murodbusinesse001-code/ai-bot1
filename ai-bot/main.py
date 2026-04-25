from flask import Flask, request
import telebot
import os

app = Flask(name)
bot = telebot.TeleBot("8216472814:AAEdb-q43nxbPVEG879z-YpTphfz2KRjQ2o")

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok"

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет!")

if name == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
