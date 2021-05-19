# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:20:32 2021

@author: Charlotte
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

