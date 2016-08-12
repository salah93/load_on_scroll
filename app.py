from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/table', methods=["GET"])
def table():
    index = int(request.args.get('index', 0))
    r = int(request.args.get('range', 50))
    table = range(100)[index: index + r]
    return json.dumps({'table': table})


if __name__ == "__main__":
    app.run(debug=True)
