"""Hug post server example."""
import datetime

import hug


@hug.post('/test')
def post_data(body):
    """Post data from hug endpoint."""
    now = str(datetime.datetime.now())[:19]
    print("GOT {}: {}".format(type(body), repr(body)))
    with open('collector.txt', 'a+', encoding='utf8') as f:
        f.write('{} <<< {}\n'.format(now, body))
