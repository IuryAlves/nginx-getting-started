# coding: utf-8

import os
from flask import Flask

app = Flask(__name__)
port = os.getenv('PORT')


@app.route("/")
def hello():
    if port == '8001':
        return "Hello from Application Server A"
    elif port == '8002':
        return "Hello from Application Server B"


if __name__ == "__main__":
    app.run("0.0.0.0", port=port)