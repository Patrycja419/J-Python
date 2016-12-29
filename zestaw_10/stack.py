#!/usr/bin/python
# -*- coding: utf-8 -*-

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      
        self.n = 0                      
        self.size = size
        self.taken = size * [False]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.taken[data]:
            return
        self.items[self.n] = data
        self.taken[data] = True
        self.n = self.n + 1

    def pop(self):
        self.n = self.n - 1
        data = self.items[self.n]
        self.taken[data] = False
        self.items[self.n] = None    
        return data
    
    def printOut(self):
        while not self.is_empty():
            print(self.pop())
       
run = Stack()
run.push(1)
run.push(1)
run.push(5)
run.push(5)
run.push(6)
run.push(9)
run.push(7)
run.printOut()
