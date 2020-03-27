#!/bin/python3

import math
import os
import random
import re
import sys

def MyBinary(n) :
    biner = bin(n)
    binering = str(biner[2:])
    spliter = binering.split("0")
    var = (sorted(spliter, reverse=True))
    var = (var[0])
    counter = 0
    for i in var:
        counter += 1
    print(counter)


if __name__ == '__main__':
    n = int(input())
    MyBinary(n)
