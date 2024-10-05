import sys

input = sys.stdin.readline

n = int(input())
maxdp = []
mindp = []

for i in range(n):
    a, b, c = map(int, input().split())

    if i == 0:
        maxdp = [a, b, c]
        mindp = [a, b, c]
        continue

    # 최대합
    maxdp = [
        a + max(maxdp[0], maxdp[1]),
        b + max(maxdp[0], maxdp[1], maxdp[2]),
        c + max(maxdp[1], maxdp[2]),
    ]

    # 최소합
    mindp = [
        a + min(mindp[0], mindp[1]),
        b + min(mindp[0], mindp[1], mindp[2]),
        c + min(mindp[1], mindp[2]),
    ]

print(max(maxdp), min(mindp))
