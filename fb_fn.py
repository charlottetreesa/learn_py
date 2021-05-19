# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:33:51 2021

@author: Charlotte
"""
def fib(n):
    a, b = 0, 1
    while a < n:
        print (a, end=" ")
        a, b = b, a+b
    print()
fib(2500)

def fibonacci(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
f = fibonacci(100)
print(f)