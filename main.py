from flask import Flask
from flask_cors import CORS
import sys
import os

# Add the current directory to sys.path to allow absolute imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes.user_routes import user_bp
from routes.yoga_routes import yoga_bp
from db_config import init_db

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Initialize database
init_db()

# Register blueprints
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(yoga_bp, url_prefix="/yoga")

@app.route("/")
def home():
    return {"message": "Yoga Backend is running"}

if __name__ == "__main__":
    print("Starting Flask server on http://0.0.0.0:8003...")
    # Update to port 8003 as provided by the user
    app.run(debug=True, host='0.0.0.0', port=8003)
