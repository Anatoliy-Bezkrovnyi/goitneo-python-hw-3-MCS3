from collections import deque

MAX_LEN = 5

lifo = deque(MAX_LEN)


def push(element):
    lifo.appendleft(element)
    


def pop():
    return lifo.popleft()