import os
from datetime import datetime
import time


def check_down_while():
    files = os.listdir("downloads")

    while any(".part" in s for s in files):
        files = os.listdir("downloads")
        time.sleep(1)
    return True

def check_down_single():
    files = os.listdir("downloads")
    
    if any(".part" in s for s in files):
        return False
    else:
        return True

val = check_down_single()

print(val)