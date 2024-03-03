import sys
from collections import deque

input = sys.stdin.readline


def check(x, y):
    global n
    global m

    queue = deque([(x, y)])
    visit[x][y] = 1
    while queue:
        x, y = queue.popleft()

        cnt = 0
        for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if a >= 0 and a < n and b >= 0 and b < m and ice[a][b] >= 1:
                if visit[a][b] == 0:
                    visit[a][b] = 1
                    queue.append((a, b))

                cnt += 1

        melt[x][y] = 4 - cnt


n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

year = 0
while True:
    no_ice = True
    check_num = 0
    visit = [[0] * m for _ in range(n)]
    melt = [[0] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ice[i][j] >= 1 and visit[i][j] == 0:
                if no_ice == True:
                    no_ice = False

                if check_num == 1:
                    check_num += 1
                    break

                check(i, j)
                check_num += 1

        if check_num == 2:
            break

    # 빙산이 아무것도 없다면 0을 출력
    if no_ice == True:
        year = 0
        break

    # 빙산이 두 덩이라면 year 출력
    if check_num == 2:
        break

    # 위 조건에 아무 것도 해당하지 않는다면 녹이기
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if ice[i][j] >= 1:
                if ice[i][j] > melt[i][j]:
                    ice[i][j] -= melt[i][j]
                else:
                    ice[i][j] = 0

    year += 1

print(year)
