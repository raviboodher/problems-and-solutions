#!/usr/bin/env python
# -*- coding: utf-8 -*-

#

class Stack:

    """
    he stack abstract data type is defined by the following structure and operations. A stack is structured, 
    as described above, as an ordered collection of items where items are added to and removed from the end 
    called the “top.” Stacks are ordered LIFO. The stack operations are given below.

    Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack.
    push(item) adds a new item to the top of the stack. It needs the item and returns nothing.
    pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
    peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.
    isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
    size() returns the number of items on the stack. It needs no parameters and returns an integer.
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


my_stack = Stack()
print my_stack.isEmpty()
my_stack.push(1)
print my_stack.isEmpty()
my_stack.push(3)
my_stack.push('one')
print my_stack.size()
print my_stack.peek()
print my_stack.pop()
print my_stack.size()
