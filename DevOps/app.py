from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from simple_math app!"


@app.route("/health")
def health():
    return "OK", 200
