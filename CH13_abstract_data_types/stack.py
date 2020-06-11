# There'd be no performance gains from using this, right? Because it's just
#   a tweaked builtin python list data structure.

class Stack:
    """A stack class."""

    def __init__(self):
        self._stack = [] # the items in the stack

    def top(self):
        """Return the item on the top of the stack (access it without popping)."""
        if len(self._stack) > 0: # can use len() builtin bc this 'stack' is just
            # a python list
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

    def is_empty(self):
        """Return true if the stack is empty, else False."""

        return len(self._stack) == 0

def main():
    mystack = Stack()
    mystack.push('one')
    print(mystack.pop())
    print(mystack.pop()) # throws the empty-stack exception

if __name__ == '__main__':
    main()
