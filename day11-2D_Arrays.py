#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    # arr = [ [-1, -1, 0, -9, -2, -2],
    #         [-2, -1, -6, -8, -2, -5],
    #         [-1, -1, -1, -2, -3, -4],
    #         [-1, -9, -2, -4, -4, -5],
    #         [-7, -3, -3, -2, -9, -9],
    #         [-1, -3, -1, -2, -4, -5] ]

    arr = [ [random.randint(-10,10) for i in range(6)] for j in range(6)]
    for i in arr:
        print(i)
    hour_sum = -9 * 6 * 6
    for i in range(4):
        for j in range(4):
            sum_= sum(arr[i][j:j+3])+arr[i+1][j+1]+sum(arr[i+2][j:j+3])
            hour_sum = max(hour_sum,sum_)
    print(hour_sum)
