from types import MethodType
from flask import Flask
app = Flask(__name__)

from flask import request

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(request.data)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()