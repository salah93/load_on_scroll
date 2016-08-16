import json
import random
import string
from flask import Flask, render_template, request
from dogpile.cache import make_region


MEMORY_CACHE = make_region().configure(
            'dogpile.cache.memory',
            expiration_time=3600)
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/table', methods=["GET"])
def table():
    index = int(request.args.get('index', 0))
    r = int(request.args.get('range', 50))
    query = request.args.get('query')
    table = do_computation(query)[index: index + r]
    return json.dumps({'table': table})


@MEMORY_CACHE.cache_on_arguments()
def do_computation(query):
    rando = [random.choice(string.ascii_letters + string.digits)
             for i in range(100)]
    print(rando)
    return rando


if __name__ == "__main__":
    app.run(debug=True)
