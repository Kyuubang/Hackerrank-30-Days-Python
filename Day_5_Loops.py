#!/bin/python3

import math
import os
import random
import re
import sys

def MyMath(n):
    for i in range(1,11):
        nums = n * i
        print(str(n),"x",str(i), "=",nums)

if __name__ == '__main__':
    n = int(input())
    MyMath(n)
