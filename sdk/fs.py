import json
from itertools import islice
from rich import print
import json_numpy
import os

def _deserizlize(i):
    raw = json_numpy.loads(i).get('p')
    return raw


def create_folder_if_not_exist(path):
    if not os.path.exists(path):
        # Create a new directory because it does not exist
        os.makedirs(path)

def read_db_file(namespace, every):
    create_folder_if_not_exist("l2db")

    if not os.path.exists(f"l2db/{namespace}"):
        return None

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
