import sys
from collections import deque

input = sys.stdin.readline

test_case = int(input())
for _ in range(test_case):
    building, rule = map(int, input().split())
    time = list(map(int, input().split()))

    indegree = [0] * building
    graph = [[] for _ in range(building)]
    for _ in range(rule):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        indegree[b - 1] += 1

    dest = int(input()) - 1

    queue = deque([])
    dp = [-1] * building

    # 진입 차수가 0인 정점찾기
    for i in range(building):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        node = queue.popleft()
        if node == dest:
            break

        for near in graph[node]:
            dp[near] = max(dp[near], dp[node] + time[near])
            indegree[near] -= 1
            # 해당 건물을 짓기 전에 지어야하는 모든 건물을 지었을 때 append
            if indegree[near] == 0:
                queue.append(near)

    print(dp[dest])
