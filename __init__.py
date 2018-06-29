if path not in sys.path:
    sys.path.append(path)
from flask import Flask
app = Flask( __name__ )

@app.route('/', methods=[ 'GET' ])
def show():
    return 'hello_world!\n', 200, { 'Content-Type': 'text/plain' }