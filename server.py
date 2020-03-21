import os
import subprocess
import json

from flask import Flask, flash, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/info")
def getUserInfo():
    cmd = 'python (ML model) [params user]'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split(b'\n')

    json_string = json.dumps({"info user": str(result)[3:len(result) - 12] })

    return json_string


@app.route("/")
def hello():
    return "Server is work"


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port = 4567)