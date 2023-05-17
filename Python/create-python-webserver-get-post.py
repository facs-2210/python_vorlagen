# Flask App
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    files = os.listdir('.')
    return jsonify(files)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(file.filename)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=8080)
