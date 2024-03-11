import time
import os
import glob
from flask import Flask, send_from_directory, abort
from flask import request
import api

files = glob.glob("./tmp/*")
for file in files:
    os.remove(file)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def drug_identify():
    f = request.files["image"]
    file_name = f"tmp/{int(time.time())}.{f.filename.split('.')[1]}"
    f.save(file_name)
    name, condition = api.analyze(file_name)
    if name is None:
        abort(404)
    return {
        "drug": name,
        "condition": condition,
        "image": "https://phqsh.tech/drug/" + file_name
    }


@app.route("/<path:path>")
def fetch_image(path):
    return send_from_directory(".", path)

