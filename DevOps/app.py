from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from simple_math app!"


@app.route("/health")
def health():
    return "OK", 200


# Ensure the app runs on the correct host and port for local testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
