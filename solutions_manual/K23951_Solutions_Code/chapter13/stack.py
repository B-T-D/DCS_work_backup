# Stack class

class Stack:
    """A stack class."""

    def __init__(self):
        self._stack = []  # the items in the stack
    
    def top(self):
        """Return the item on the top of the stack."""

        if len(self._stack) > 0:
            return self._stack[-1]
        raise IndexError('stack is empty')
    
    def pop(self):
        """Return and delete the item on the top of the stack."""

        if len(self._stack) > 0:
            return self._stack.pop()
        raise IndexError('stack is empty')
    
    def push(self, item):
        """Insert a new item on the top of the stack."""

        self._stack.append(item)
        
    def isEmpty(self):
        """Return true if the stack is empty, false otherwise."""

        return len(self._stack) == 0
