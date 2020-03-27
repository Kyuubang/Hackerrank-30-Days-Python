# # #!/bin/python3
#
# import math
# import os
# import random
# import re
# import sys
#
# def collectTolist(arr):
#     List = []
#     for i in arr:
#         for x in range(4):
#             List.append(i[:3])
#
# if __name__ == '__main__':
#     arr = []
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     maxSum(arr)
#

List = [[1,1,1,0,0,0],
        [0,1,0,0,0,0],
        [1,1,1,0,0,0],
        [0,0,2,4,4,0],
        [0,0,0,2,0,0],
        [0,0,1,2,4,0]]

array = List


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


var = (Heading(array))
for i in var:
    print(i)
