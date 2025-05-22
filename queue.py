class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return  len(self.items) == 0
    def enqueue(self, items):
        self.items.append(items)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(13)
queue.enqueue("Exit")
queue.enqueue(False)
queue.enqueue(13.13)
print(queue.peek())         # 13
print(queue.size())         # 4
print(queue.is_empty())     # False
queue.dequeue()
queue.dequeue()
print(queue.size())         # 2
print(queue.peek())         # False
queue.enqueue(15)
print(queue.peek())         # False
queue.dequeue()
queue.dequeue()
print(queue.peek())         # 15
queue.dequeue()
print(queue.is_empty())     # True

