#!/usr/bin/env python


class Queue:

    """
    A queue stores items in a first-in, first-out (FIFO) order.

    Before we begin implementing our own queue, let's review the attribute and methods it will have:
    Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
    enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
    dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
    isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
    size() returns the number of items in the queue. It needs no parameters and returns an integer.
 
    """


    def __init__(self):
        """
        creates a new queue that is empty. It needs no parameters and returns an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        adds a new item to the rear of the queue. It needs the item and returns nothing.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
        """
        return self.items.pop()

    def isEmpty(self):
        """
        tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
        """
        return self.items == []

    def size(self):
        """
        returns the number of items in the queue. It needs no parameters and returns an integer.
        """
        return len(self.items)


q = Queue()
print q.size()
print q.isEmpty()
q.enqueue(1)
q.enqueue('two')
print q.size()
print q.dequeue()
