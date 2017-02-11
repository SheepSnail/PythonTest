#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def letter_count(str):
    counts = {}
    result = []
    for x in str:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for x in counts:
        result.append((x,counts[x]))
    return result

str = input('请输入一串字母：')  
print(letter_count(str))
