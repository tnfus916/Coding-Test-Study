import sys

# from collections import deque
import heapq

input = sys.stdin.readline


def bfs(x, y):
    global n
    size = 2
    ate = 0
    graph[x][y] = 0  # 아기 상어가 있던 자리 0으로 세팅
    heap = [(x, y, 0)]
    visit = [[0] * n for _ in range(n)]
    visit[x][y] = 1
    time = 60
    while heap and time < 70:
        x, y, time = heapq.heappop(heap)
        visit[x][y] = 1
        print("pop", x, y, time)

        # 해당 공간에 있는 물고기를 먹어도 될 때
        if graph[x][y] < size and graph[x][y] != 0:
            graph[x][y] = 0

            # 초기화
            heap = [(x, y, time)]
            visit = [[0] * n for _ in range(n)]
            visit[x][y] = 1
            ate += 1
            if ate == size:  # 아기 상어의 크기와 같은 수의 물고기를 먹었다면 커진다.
                size += 1
                ate = 0
            print("eat", x, y, size, time, heap)
            continue

        print("push", end=" ")
        # 상좌우하 순으로 확인
        for a, b in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
            if a >= 0 and a < n and b >= 0 and b < n:
                # 물고기가 없거나 물고기 크기가 상어보다 같거나 작을 때 heap에 삽입
                if graph[a][b] <= size and visit[a][b] == 0:
                    visit[a][b] = 1
                    print(a, b, time + 1, end="  -  ")
                    heapq.heappush(heap, (a, b, time + 1))
        print()

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


n = int(input())

graph = []
shark = (-1, -1)
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    if 9 in arr:
        shark = (i, arr.index(9))

print(bfs(shark[0], shark[1]))
