from flask import Flask

app = Flask(__name__)

# Главная страница (уберёт 404)
@app.route("/")
def home():
    return "Сайт работает ✅"

# Пример для бота (можно менять потом)
@app.route("/webhook")
def webhook():
    return "Webhook работает 🤖"

# Важно для Railway
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
