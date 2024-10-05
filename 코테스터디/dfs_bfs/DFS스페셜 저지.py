import sys
from collections import deque

input = sys.stdin.readline


def check_dfs(node):
    global cnt

    if result[cnt] != node + 1:
        return

    for near in graph[node]:
        if visit[near] == 0:

            visit[near] = 1
            cnt += 1
            check_dfs(near)
            visit[near] = 0
            cnt -= 1


n = int(input())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    srt, end = map(int, input().split())
    graph[srt - 1].append(end - 1)
    graph[end - 1].append(srt - 1)

result = list(map(int, input().split()))

visit = [0] * n

if result[0] != 1:
    print(0)
else:
    cnt = 0
    check_dfs(0)
    print(0)
