# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
arr = {}
for i in range(n):
    name,phone = input().split(' ')
    arr[name] = phone


inputs = sys.stdin.readlines()

for i in inputs:
    text = i.strip()
    if text in arr:
        print(f'{text}={arr[text]}')
    else:
        print('Not found')
        