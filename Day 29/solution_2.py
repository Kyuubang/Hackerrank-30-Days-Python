#!/bin/python3
# before you use this solution you should find brute force solution!!
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())


    for _ in range(t):
        n , k = map(int , input().split())
        # print(k-1 if ((k-1) | k) <= n else k-2)
        if (k-1 | k) <= n:
            print(k-1)
        else :
            print(k-2)
