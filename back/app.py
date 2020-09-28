# coding=UTF-8
from flask import Flask, json, make_response, request
from flask_cors import CORS
import os
from http import HTTPStatus
from flask_mongoengine import MongoEngine

app = Flask(__name__)
CORS(app)

GENERIC_DESCRIPTION = "Sorry :( Something happened here! Someone should have dropped soda in the keyboard but everything will be clean soon"
from config.log import Log

log = Log("ROUTE")


def jsonify(data):
    return json.dumps(data, ensure_ascii=False).encode("utf8")


@app.route("/health", methods=["GET"])
def health():
    return make_response(jsonify("Hello World! Blockchain"), HTTPStatus.OK.value)


@app.route("/blocks", methods=["POST"])
def login():
    pass


@app.route("/blocks", methods=["GET"])
def login():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.getenv("APPLICATION_PORT"))
