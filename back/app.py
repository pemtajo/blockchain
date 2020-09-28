# coding=UTF-8
from flask import Flask, json, make_response, request
from flask_cors import CORS
import os
from http import HTTPStatus

app = Flask(__name__)
CORS(app)

GENERIC_DESCRIPTION = "Sorry :( Something happened here! Someone should have dropped soda in the keyboard but everything will be clean soon"
from config.log import Log
from models.blockchain import BlockChain

log = Log("ROUTE")

blockchain = BlockChain()


def jsonify(data):
    return json.dumps(data, ensure_ascii=False).encode("utf8")


@app.route("/health", methods=["GET"])
def health():
    return make_response(jsonify("Hello World! Blockchain"), HTTPStatus.OK.value)


@app.route("/blocks", methods=["POST"])
def addBlock():
    req = request.json
    blockchain.generateBlock(req["data"])
    return make_response(
        jsonify("Add data " + json.dumps(req["data"])), HTTPStatus.OK.value
    )


@app.route("/blocks", methods=["GET"])
def getAllBlocks():
    return jsonify(blockchain.returnAllBlocks())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=os.getenv("APPLICATION_PORT"))
