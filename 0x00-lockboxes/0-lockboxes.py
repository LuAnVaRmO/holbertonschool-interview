#!/usr/bin/python3
"""
Determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """ Check boxes """
    keys = boxes[0]
    for k in keys:
        openbox = boxes[k]
        for nk in openbox:
            if nk not in keys and nk > 0:
                keys.append(nk)
    if len(keys) == len(boxes) - 1:
        return True
    return False
