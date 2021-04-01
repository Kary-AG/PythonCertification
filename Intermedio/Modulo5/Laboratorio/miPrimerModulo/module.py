#!/usr/bin/env python3
"""module.py - an example of Python module"""
__counter = 0

def suml(list):
    global __counter
    __counter +=1
    sum = 0
    for el in list:
        sum+=el
    return sum
def prodl(list):
    global __counter
    __counter +=1
    prod = 1
    for el in list:
        prod *= el
        return prod

if __name__=="__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(sum(l)==15)
    print(prodl(1)==120)
