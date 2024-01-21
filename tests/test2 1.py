from threading import Thread

import numpy as np
from rich import print
from rich.prompt import Prompt
from sdk.datasets.for_small_test import all_messages
from sdk.datasets.girl_about_parents import DATASET_GIRL_ABOUT_PARENTS, filter_girl_messages
from sdk.modules.context_to_3d import context_to_3d
from sdk.modules.scan_closest_points_and_links import scan_closest_points_and_links
from sdk.modules.throws import EmptyContext, InsufficientContext

if __name__ == '__main__':
    array = []
    mode = 'MSG'  # or SEARCH
    
    # dataset = [
    #     "I bought a new car and now I can go to the mountains",
    #     "I'm thinking of going to the mountains on Monday",
    #     "I went to the mountains",
    #     "I read a lot about the Himalayas, they say it’s a great place to relax",
    #     "In general, the Himalayas are my dream",
    #     "I was there as a child with my mother"
    # ]
    
    dataset = filter_girl_messages(DATASET_GIRL_ABOUT_PARENTS)
    
    t = 0
    for msg in dataset:
        t += 1
        print(f"Training... [{t}/{len(dataset)}]")
        array.append(context_to_3d(msg))
    
    while True:
        phrase = Prompt.ask(f"$({mode})")
        
        if phrase == 'SEARCH' or phrase == 'MSG':
            mode = phrase
            continue
    
        try:
            axis = context_to_3d(phrase)
        except EmptyContext:
            print("Empty context")
            axis = None
        except InsufficientContext:
            print("Insufficient context")
            axis = None
        
        if axis and mode == 'MSG':
            array.append(axis)
             
        if axis and mode == 'SEARCH':
            for query in axis[1]:
                print(
                    scan_closest_points_and_links(
                        array,
                        [
                            np.float32(query[0][0]),
                            np.float32(query[0][1]),
                            np.float32(query[0][2]),
                            query[1],
                        ],
                        0.000001
                    )
                )
        
        print(axis)
        
        