from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

zero = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

safe_area = 0
wall = n * m - len(zero) - len(virus) + 3

for zeros in combinations(zero, 3):
    # 3개의 벽을 세워서 안전 영역 구하기
    for i, j in zeros:
        graph[i][j] = 1

    # bfs
    queue = deque(virus)
    visit = [[0] * m for _ in range(n)]
    for i, j in virus:
        visit[i][j] = 1

    virus_cnt = len(virus)
    while queue:
        i, j = queue.popleft()

        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if x >= 0 and x < n and y >= 0 and y < m:
                if visit[x][y] == 0 and graph[x][y] == 0:
                    visit[x][y] = 1
                    queue.append((x, y))
                    virus_cnt += 1

    safe_area = max(safe_area, n * m - wall - virus_cnt)

    # 3개의 벽 허물기
    for i, j in zeros:
        graph[i][j] = 0

print(safe_area)
