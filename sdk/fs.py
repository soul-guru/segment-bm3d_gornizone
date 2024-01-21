import json
from itertools import islice
from rich import print
import json_numpy

def _deserizlize(i):
    raw = json_numpy.loads(i).get('p')
    return raw


def read_db_file(namespace, every):
    with open(f"l2db/{namespace}", 'r+') as file:
        while True:
            lines = list(islice(file, 100))
            _list = list(map(_deserizlize, lines))
                
            if _list:
                print(_list)
                every(_list)

            for line in lines:
                pass
                # everyline
            if not lines:
                break
