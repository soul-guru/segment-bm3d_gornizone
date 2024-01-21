import time
from secrets import token_hex
from rich import print

import numpy as np

from sdk.modules.classification_vector import classification_vector
from sdk.modules.sentence_to_3d_coordinates import sentence_to_3d_coordinates
from sdk.modules.split_into_parts import split_into_parts
from sdk.modules.throws import EmptyContext, InsufficientContext
from sdk.profile import profiler_point, profiler_close_point


def context_to_3d(
        text: str,
        skip_summary: bool = False,
        skip_split: bool = False,
        skip_vector_classification: bool = False
):
    if len(text) == 0:
        raise EmptyContext
    
    if len(text) < 18:
        raise InsufficientContext
    
    out: list[((np.float32, np.float32, np.float32), float, str)] = []

    point_for = profiler_point("for phrase in split_into_parts")
    
    if not skip_split:
        point = profiler_point("split_into_parts(text, False, skip_summary)")
        texts = split_into_parts(text, False, skip_summary)
        profiler_close_point(point)
    else:
        texts = [text]
        
    for phrase in texts:
        if len(phrase) <= 3:
            continue
    
        point = profiler_point("sentence_to_3d_coordinates")
        x, y, z = sentence_to_3d_coordinates(phrase)
        profiler_close_point(point) 
        
        point = profiler_point("classification_vector")
        if not skip_vector_classification:
            v = classification_vector(phrase)
        else:
            v = 0
        profiler_close_point(point)
        
        out.append(((x, y, z), v, phrase))
    profiler_close_point(point_for)

    return token_hex(16), out
