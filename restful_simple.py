from flask import Flask, jsonify, make_response
import flask
import json

app = Flask(__name__)

@app.route('/')
def index():
    resp = {'Hello':'World!'}
    return make_response(jsonify(resp))

if __name__ == '__main__':
    app.run(debug=True)