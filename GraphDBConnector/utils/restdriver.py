from flask import Flask,jsonify
from driver import get_result
app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route("/")
def hello():
    # return "Hello World!"
    return jsonify(payload = get_result())
    # return jsonify(payload={'greeting':'hello'})

if __name__ == "__main__":
    app.run(debug=True)