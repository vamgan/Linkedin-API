from flask import Flask, request, jsonify
from linkedin import getJob
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])

def jobs():
    if request.method == 'POST':
        return jsonify(getJob(request.form['role']))
    elif request.method == 'GET':
        return jsonify(getJob(request.args.get('role')))

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True)
