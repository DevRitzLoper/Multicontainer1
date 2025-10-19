import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'postgresql://postgres:devcontainer@db:5432/postgres'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/api")
def api():
    return jsonify(message="Hello from backend API")

@app.route("/health")
def health():
    try:
        # Test database connection
        db.session.execute('SELECT 1')
        return jsonify(
            status="healthy",
            message="API and database connection are working"
        )
    except Exception as e:
        return jsonify(
            status="unhealthy",
            message=str(e)
        ), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)