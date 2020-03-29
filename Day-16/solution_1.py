#!/bin/python3

import sys


S = input().strip()
try :
    operation = int(S)
    print(operation)
except ValueError:
    print("Bad String")
