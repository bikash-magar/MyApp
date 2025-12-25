from flask import Flask, jsonify
from flask_cors import CORS  # Add this import
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/name')
def get_name():
    return jsonify({'name': 'Bikash Magar'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000
    app.run(host='0.0.0.0', port=port, debug=False)  # Disable debug for production