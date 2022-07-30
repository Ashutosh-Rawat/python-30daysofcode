#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    x = str(bin(n)[2:])
    count=0
    max_count=0
    
    for i in x:
        if i=='1':
            count+=1
        else:
            max_count = max(count,max_count)
            count=0
    max_count = max(count,max_count)
    print(max_count)