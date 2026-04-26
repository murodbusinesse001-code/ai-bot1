from flask import Flask, request

app = Flask(_name_)

@app.route('/')
def home():
    return "Bot is working"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(data)
    return "OK", 200

if name == "main":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
gunicorn -X POST https://Ollama.railway.app/api
func main() {
  // ...
  // Use `PORT` provided in environment or default to 3000
  port := cmp.Or(os.Getenv("PORT"), 3000)

  log.Fatal(http.ListenAndServe((":" + port), handler))
  // ...
}
