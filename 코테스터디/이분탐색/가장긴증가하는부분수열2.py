import sys

input = sys.stdin.readline


def bin_search(srt, end, target):
    while srt < end:
        mid = (srt + end) // 2
        if target < stack[mid]:
            end = mid
        elif target > stack[mid]:
            srt = mid + 1
        else:
            return mid
    return end


n = int(input())
arr = list(map(int, input().split()))

stack = [arr[0]]
for i in range(1, n):
    if arr[i] > stack[-1]:
        stack.append(arr[i])
    elif arr[i] < stack[-1]:
        stack[bin_search(0, len(stack) - 1, arr[i])] = arr[i]

print(len(stack))

# bisect 사용한 풀이

# import sys
# import bisect

# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# stack = [arr[0]]
# for i in range(1, n):
#     if arr[i] > stack[-1]:
#         stack.append(arr[i])
#     else:
#         stack[bisect.bisect_left(stack, arr[i])] = arr[i]

# print(len(stack))
