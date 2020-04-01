#!/bin/python3

import math
import os
import random
import re
import sys

def Heading(arr):
    midNums = []
    for i in range(1,(len(array)-1)):
        for _ in range(1, (len(array)-1)):
            midNums.append(array[i][_])
            continue
    Listing = []
    for i in range(len(arr)):
        for _ in range(4):
            Listing.append(arr[i][:3])
            del arr[i][0]
            continue

    for i in range(len(Listing)-1):
        for i in range()
    return Listing

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print (maxSum(arr))
