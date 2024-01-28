# 이렇게 for문을 이용해 상좌우하 순으로 queue에 삽입했다고 해도 깊이가 깊어지면 현재 위치의 우상보다 좌하에 위치하는 공간에 먼저 진입하게 되므로 틀린 풀이이다.

import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    global n
    size = 2
    ate = 0
    graph[x][y] = 0  # 아기 상어가 있던 자리 0으로 세팅
    queue = deque([(x, y, 0)])
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1

    while queue:
        x, y, time = queue.popleft()

        # 엄마 상어 부를지 체크
        breakcheck = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] < size and graph[i][j] > 0:
                    breakcheck = 1
                    break
            if breakcheck == 1:
                break
        if breakcheck == 0:
            return time

        # 상좌우하 순으로 확인
        for a, b in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
            if a >= 0 and a < n and b >= 0 and b < n and visit[a][b] == 0:

                # 물고기가 없거나 물고기 크기가 상어보다 같을 때 지나간다.
                if graph[a][b] == 0 or graph[a][b] == size:
                    queue.append((a, b, time + 1))
                    visit[a][b] = 1

                # 물고기 크기가 상어보다 작을 때 먹는다.
                elif graph[a][b] < size:
                    graph[a][b] = 0  # 해당 공간은 빈 공간이 됨
                    queue = deque([(a, b, time + 1)])
                    visit = [[0] * n for _ in range(n)]
                    visit[a][b] = 1
                    ate += 1
                    if ate == size:  # 아기 상어의 크기와 같은 수의 물고기를 먹었다면 커진다.
                        size += 1
                        ate = 0
                    break

                # 물고기 크기가 상어보다 클 때, graph[a][b]>size 일 때는 지나갈 수 없다.
                else:
                    visit[a][b] = 1
                    continue


n = int(input())

graph = []
shark = (-1, -1)
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    if 9 in arr:
        shark = (i, arr.index(9))

print(bfs(shark[0], shark[1]))
