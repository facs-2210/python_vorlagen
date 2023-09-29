# Python Flask Webserver GET and POST

## Run Script
```python
python ./flask-app.py
```

## List directory using curl
`curl http://localhost:5000/list`

## Upload using curl
`curl -X POST -F 'file=@./path/to/filename' http://127.0.0.1:5000/upload`

## Download using curl
`curl -O http://localhost:5000/download/filename`