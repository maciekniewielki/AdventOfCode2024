import os
import sys
import importlib
sys.path.append(os.curdir)

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print("Please provide day number")
        exit()
    folder_name = f"day{sys.argv[1].zfill(2)}"
    try:
        os.chdir(os.path.join(sys.path[0], folder_name))
        importlib.import_module(folder_name)
    except FileNotFoundError:
        print("Day not found")