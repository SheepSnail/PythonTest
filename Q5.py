#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Queue(object):
    def __init__(self):
        self.dataList = []

    def enqueue(self, value):
        self.dataList.append(value)

    def dequeue(self):
        return self.dataList.pop(0)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue()) # 1
print(q.dequeue()) # 2
print(q.dequeue()) # 3
