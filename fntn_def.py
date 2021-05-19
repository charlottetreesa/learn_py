# -*- coding: utf-8 -*-
"""
Created on Thu May 20 01:53:04 2021

@author: Charlotte
"""
def fn_def(prompt, chance=4, reminder='try again!'):
    while True:
        read_val = input(prompt)
        if read_val in ('a' , 'b', 'c', 'd'):
            return True
        if read_val in ('e', 'f', 'g', 'h'):
            return False
        chance = chance-1
        if chance < 0:
            raise ValueError('invalid input')
        print (reminder)
fn_def('enter an alphabet')
