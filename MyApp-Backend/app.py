from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/name')
def get_name():
    return jsonify({'name': 'Bikash Magar'})  # Replace with dynamic data if needed

if __name__ == '__main__':
    app.run(debug=True)