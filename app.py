import json
import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/table', methods=["GET"])
def table():
    index = int(request.args.get('index', 0))
    r = int(request.args.get('range', 50))
    table = do_computation()[index: index + r]
    return json.dumps({'table': table})


def do_computation():
    rando = [random.choice(string.ascii_letters + string.digits)
             for i in range(100)]
    print(rando)
    return rando


if __name__ == "__main__":
    app.run(debug=True)
