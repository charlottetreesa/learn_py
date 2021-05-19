# -*- coding: utf-8 -*-
"""
Created on Thu May 20 00:52:43 2021

@author: Charlotte
"""
words = ['abc', 'xyz', 'pqrs', 'cdefg']
print('for loop demo for list ')
for w in words:
    print(w, len(w))
print('for loop demo for range(i) ')
for i in range(10):
    print(i, end=" ")
print()
print('for loop demo for range(start,end) ')
for i in range(5,10):
    print(i,end=' ')
print()
print('for loop demo for range(start, stop, step) ')
for i in range(0,10, 3):
    print(i, end=' ')
print()
a = ['a', 'complete', 'sentence', 'here']
for i in range(len(a)):
    print(i, a[i])
print(sum(range(4)))
print(list(range(4)))

    
