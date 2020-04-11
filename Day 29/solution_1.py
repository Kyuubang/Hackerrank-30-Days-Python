#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())

    for t_itr in range(t):
        nk = int(sys.stdin.readline().strip().split())

        n = int(nk[0])
        k = int(nk[1])

        A = ([x for x in range(1,n+1)])
        B = A
        bit = 0
        for i in range(n):
            for j in range(n):
                if A[i] < B[j]:
                    x = (A[i] & B[j])
                    if x < k and x > bit:
                        bit = x
        print(bit)

        input().split()
