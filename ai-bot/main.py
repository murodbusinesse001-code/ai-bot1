
@app.route('/')
def home():
    return "Hello from Railway!"

app.run(host='0.0.0.0', port=3000)