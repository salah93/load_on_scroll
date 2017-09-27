import json
import random
import string
from dogpile.cache import make_region
from flask import Flask, render_template, request


MEMORY_CACHE = make_region().configure(
            'dogpile.cache.memory',
            expiration_time=3600)
app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/table', methods=["GET"])
def table():
    r = int(request.args.get('range', 100))
    table = do_computation(r)
    print 'table = %s' % ', '.join([str(i) for i in table])
    return json.dumps({'table': table})


@MEMORY_CACHE.cache_on_arguments()
def do_computation(value):
    r = [i for i in xrange(value)]
    print 'r = %s' % ', '.join([str(i) for i in r])
    return r


if __name__ == "__main__":
    app.run("localhost", port=6543)
