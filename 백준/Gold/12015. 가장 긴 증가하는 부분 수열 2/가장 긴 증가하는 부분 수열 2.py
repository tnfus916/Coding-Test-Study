import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]
for i in range(1, n):
    if arr[i] > stack[-1]:
        stack.append(arr[i])
    else:
        stack[bisect.bisect_left(stack, arr[i])] = arr[i]

print(len(stack))
