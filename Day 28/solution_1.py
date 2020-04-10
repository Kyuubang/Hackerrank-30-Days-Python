#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    pattern = r"@gmail.com"
    List = []
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if re.search(pattern, emailID):
            List.append(firstName)
    List.sort()
    for i in (List):
        print(i)
