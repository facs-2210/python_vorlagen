#!/usr/bin/python3
import zlib
import sys
import json
from itsdangerous import base64_decode


def decode(cookie):
    """
    Decode a Flask cookie

    https://www.kirsle.net/wizards/flask-session.cgi
    """
    try:
        compressed = False
        payload = cookie

        if payload.startswith('.'):
            compressed = True
            payload = payload[1:]

        data = payload.split(".")[0]

        data = base64_decode(data)
        if compressed:
            data = zlib.decompress(data)

        return data.decode("utf-8")
    except Exception as e:
        return f"[Decoding error: are you sure this was a Flask session cookie? {e}]"


cookie = sys.argv[1]
data = decode(cookie)
json_data = json.loads(data)
pretty = json.dumps(json_data, sort_keys=True, indent=4, separators=(",", ": "))
print(pretty)