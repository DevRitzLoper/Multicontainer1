import flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def api():
    return jsonify(message="Hello from backend API")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)