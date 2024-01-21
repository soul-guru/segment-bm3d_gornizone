import os
import time

from rich import print


def profiler_point(point_name: str):
    if os.environ.get('PROFILER_ENABLED', 'false') == 'true':
        t = time.process_time()

        return point_name, t


def profiler_close_point(point: (str, float)):
    if os.environ.get('PROFILER_ENABLED', 'false') == 'true':
        elapsed_time = time.process_time() - point[1]

        print(f"📍 [{'{0: <6}'.format(round(elapsed_time, 4))} s]: {point[0]}")
