from flask import Flask, request

app = Flask(name)

@app.route('/')
def home():
    return "Bot is working"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)  # чтобы видеть, что приходит
    return "OK", 200
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
