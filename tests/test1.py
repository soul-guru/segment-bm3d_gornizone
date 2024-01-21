from rich import print

from sdk.datasets.for_small_test import all_messages
from sdk.modules.context_to_3d import context_to_3d

if __name__ == '__main__':
    for s in reversed(all_messages):
        axis = context_to_3d(s)
        
        print(f"AXIS for '{s}':")
        print(f"g={axis[0]}")
        print("a=(see below)")
        print(axis[1])
        print("-----------")
        