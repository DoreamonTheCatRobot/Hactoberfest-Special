# Creating a queue
def create_queue():
    queue = []
    return queue

def check_empty(queue):
    return len(queue) == 0

# Adding items into the queue
def enqueue(queue, item):
    queue.append(item)
    
# Removing an element from the queue
def dequeue(queue):
    if (check_empty(queue)):
        return "queue is empty"

    return queue.pop(0)


queue = create_queue()