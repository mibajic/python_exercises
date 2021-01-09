from collections import deque


# my_queue = deque()
# my_queue.append(5)
# my_queue.append(10)
# my_queue.append(15)
# my_queue.append(20)
# print(my_queue)
# print(my_queue.pop())
# print(my_queue.popleft())

class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        return self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def get_size(self):
        return len(self.queue)