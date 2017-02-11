#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def find_word(str, begin):
    end = begin
    while end < len(str) and (not str[end].isspace()):
        end += 1
    return str[begin:end]

def format_word(word):
    if len(word) > 0:
        return word[0].upper() + word[1:].lower()
    else:
        return word

def cap_string(str):
    n=len(str)
    x = 0
    while x < n:
        if str[x].isalpha():
            word = find_word(str, x)
            newWord = format_word(word)
            str = str.replace(word, newWord, 1)
            x += len(word)
        else:
            x += 1
    return str

sentence = 'GOD IS A GIRL.'
print(cap_string(sentence))
