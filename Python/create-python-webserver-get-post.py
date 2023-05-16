# POST
# curl -X POST -F 'file=@/path/to/file' http://localhost:8080/upload
# GET
# curl http://localhost:8080/

import os
import asyncio
from aiohttp import web
from flask import Flask, request, jsonify

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

async def init():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
