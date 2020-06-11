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

    def other__str__(self): # mine
        """Return a string representation of the stack, indicating which end
        of the stack is the top, and whether the stack is empty."""
        string_start = '{ Top--> '
        string_end = ' -->Bottom }'
        string_mid = ''
        if len(self._stack) == 0:
            string_mid = 'Stack is empty'
        else:
            copy_stack = self._stack.copy()
            for item in copy_stack:
                string_mid = item + ', ' + string_mid
        return string_start + string_mid + string_end

    def __str__(self): # book's
        if len(self._stack) == 0: # can call len directly on self?
            stack_string = '| (empty) |'
        else:
            stack_string = '| '
            for item in self._stack:
                stack_string = stack_string + repr(item) + ' | '
                # NB classes can also define their own __repr__() method,
                #   same as __str__()
        return stack_string + '<-top'

    # Difference between __str__ and __repr__ is that repr is expected to return
    #   a valid python expression, while str isn't. 
            

def main():
    mystack = Stack()
    mystack.push('one')
    print(mystack.pop())
##    print(mystack.pop()) # throws the empty-stack exception

    test_stack = Stack()
    print(f"test stack printed while empty:\n\t{test_stack}")
    for letter in list('ABCD'):
        print(letter)
        test_stack.push(letter)
    print(test_stack)
    print(f"test_stack.pop should return same thing as shows up at 'top' \
in the string representation:\n\t{test_stack.pop()}")

if __name__ == '__main__':
    main()
