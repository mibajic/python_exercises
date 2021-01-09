my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack.pop())
print(my_stack.pop())


class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    # string representation of list
    def __str__(self):
        return str(self.stack)


# test code
my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
my_stack.push(5)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack.pop())
