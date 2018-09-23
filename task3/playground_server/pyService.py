from flask import Flask, request, Response
import json
import os
import sys
from io import StringIO
import logging
import traceback
import subprocess

app = Flask(__name__, static_url_path='')


@app.route("/py/eval", methods=['GET', 'POST'])
def handle():
    if request.method == 'POST':

        # Implementation goes here.
        #
        # Both stdout and stderr should be captured.
        # {"stdout": "<output_from_stdout>", "stderr": "<output_from_stderr>"}

        # code = request.json['code']
        # received_data = request.get_json()
        # code = received_data['code']
        if request.headers['Content-Type'] == 'application/json':
            code = request.json['code']
        else:
            code = request.form['code']

        code_file = open("code.py", "w+")
        code_file.write(code)
        code_file.close()

        proc = subprocess.Popen(['python3', 'code.py'],
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)

        try:
            output = proc.communicate(timeout=15)
            outs = output[0].decode("utf-8")
            errs = output[1].decode("utf-8")
        except TimeoutExpired:
            proc.kill
            output = proc.communicate()
            outs = output[0].decode("utf-8")
            errs = output[1].decode("utf-8")

        ret = {"stderr": errs, "stdout": outs}
        ret_js = json.dumps(ret, sort_keys=True)
        response = Response(response=ret_js,
                            status=200,
                            mimetype='application/json')
        return response


if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)
