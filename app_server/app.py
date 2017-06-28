# coding: utf-8

import os
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    env = os.getenv('ENV')
    return "Hello from Application Server {0}".format(env)


if __name__ == "__main__":
    port = os.getenv('PORT')
    app.run("0.0.0.0", port=port)