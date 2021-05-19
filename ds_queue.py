# -*- coding: utf-8 -*-
"""
Created on Thu May 20 03:08:25 2021

@author: Charlotte
"""
#using collections.deque for efficiency , list requires shifting of elements
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.append(5)
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)