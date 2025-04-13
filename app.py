from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from simple_math app!"


@app.route("/health")
def health():
    return "OK", 200


# Ensure the app runs on the correct host and port for Heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # THIS IS IMPORTANT
    app.run(host="0.0.0.0", port=port)
