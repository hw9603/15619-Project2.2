from flask import Flask, request, Response, make_response, jsonify
import requests
import logging
import json

# pythonServiceHostName = "http://35.185.94.101/py/eval"
pythonServiceHostName = "http://project22task3:80/py/eval"

app = Flask(__name__, static_folder='site', static_url_path='')


@app.route("/", methods=['GET'])
def handle():
    return app.send_static_file("index.html")


@app.route("/python", methods=['GET', 'POST'])
def handlePython():
    if request.method == 'POST':

        # This should return the stdout and stderr in json format
        # return the exact response from pyService.py only!
        # Your code should handle 'code' as an argument in both
        # request.form and request.json
        if request.headers['Content-Type'] == 'application/json':
            code = request.json['code']
        else:
            code = request.form['code']
        # if request.json is None:
        #     code = request.form['code']
        # else:
        #     code = request.json['code']

        req_body = {"code": code}
        res = requests.post(pythonServiceHostName,
                            data=json.dumps(req_body),
                            headers={'Content-Type':
                                     'application/json'})
        res_json = jsonify(res.json())
        return res_json
    else:
        return app.send_static_file("python.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
