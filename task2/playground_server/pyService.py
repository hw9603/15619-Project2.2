from flask import Flask, request, Response
import json
import os, sys
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
        # {"stdout": "Hello 15619!", "stderr": ""}
        #
        # Sample input: {"code": "print("Hello 15619!")"}

        ### BEGIN STUDENT CODE ###
        # stdout = sys.stdout
        # stderr = sys.stderr
        # sys.stdout = StringIO()
        # sys.stderr = StringIO()
        # redirected_output = sys.stdout
        # redirected_error = sys.stderr

        received_data = request.get_json()
        code = received_data['code']

        code_file = open("code.py", "w+")
        code_file.write(code)
        code_file.close()

        proc = subprocess.Popen(['python3', 'code.py'], \
                          stderr = subprocess.PIPE, \
                          stdout = subprocess.PIPE)

        try:
            outs, errs = proc.communicate(timeout=15)
        except TimeoutExpired:
            proc.kill
            outs, errs = proc.communicate()

        # if outs == None:
        #     outs = ""
        # if errs == None:
        #     errs = ""

        # out, err, exc = None, None, None

        # try:
        #     exec(code)
        # except:
        #     exc = traceback.format_exc()

        # out = redirected_output.getvalue()
        # err = redirected_error.getvalue()

        # sys.stdout = stdout
        # sys.stderr = stderr

        ret = {"stderr": errs, "stdout": outs}
        ret_js = json.dumps(ret)
        response = Response(response = ret_js,
                            status = 200,
                            mimetype = 'application/json')
        return response


        ### END STUDENT CODE ###

if __name__ == '__main__':
    app.run(threaded=True, debug=True, host="0.0.0.0", port=6000)

