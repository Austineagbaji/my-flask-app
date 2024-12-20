from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Banking App!"

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
