from flask import Flask, request, send_from_directory, jsonify
import os

UPLOAD_DIRECTORY = './uploads'  # Directory to store uploaded files

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join(UPLOAD_DIRECTORY, filename))
    return f"File '{filename}' uploaded successfully!"

@app.route('/list', methods=['GET'])
def list_files():
    files = os.listdir(UPLOAD_DIRECTORY)
    return jsonify(files)

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(UPLOAD_DIRECTORY, filename, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    app.run()
