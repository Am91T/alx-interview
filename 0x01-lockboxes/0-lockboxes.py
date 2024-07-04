#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    opened = set([0])
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key not in opened and key < n:
                opened.add(key)
                queue.append(key)

    return len(opened) == n
