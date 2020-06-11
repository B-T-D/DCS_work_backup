class Queue:
    """Implements a queue abstract data type."""

    def __init__(self):
        self._queue = []

    def front(self):
        return self._queue[0]

    def dequeue(self):
        return self._queue.pop(0)

    def enqueue(self, item):
        self._queue.append(item)

    def is_empty(self):
        return len(self._queue) == 0

    def __str__(self):
        return '(q first -->' + repr(self._queue) + 'q)'
        
