queue = []

def enqueue(value):
    queue.append(value)

def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        return None

def is_empty():
    return len(queue) == 0

def display():
    for item in queue:
        print(item)
    print()
