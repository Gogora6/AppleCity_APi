from flask import Flask, jsonify
from functions import login_website

app = Flask(__name__)


@app.route("/email=<string:email>&password=<string:password>", methods=['GET'])
def login(email, password):
    info = login_website(email, password)
    if not info:
        return jsonify({"status": 401, "message": 'bad credentials'})
    else:
        return jsonify({"status": 200, "message": info})


if __name__ == '__main__':
    app.run(debug=False, port=4000)
