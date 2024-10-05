import sys
from collections import deque
import copy

sys.recursionlimit(10000)
input = sys.stdin.readline


def dfs(x, y):
    visit[x][y] = 1

    for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if a >= 0 and a < n and b >= 0 and b < m:
            if tmp[a][b] >= 1 and visit[a][b] == 0:
                dfs(a, b)

    return


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] >= 1:
            ice.append((i, j))

year = 0
while len(ice) > 0:

    dfs_cnt = 1
    visit = [[0] * m for _ in range(n)]
    for x, y in ice:
        if visit[x][y] == 0:
            if dfs_cnt == 2:
                print(year)
                break
            dfs(x, y)
            dfs_cnt += 1

    if dfs_cnt == 2:
        break
    year += 1

    tmp = copy.deepcopy(ice)

    # 덩어리 개수 세기

    check_num = 0  # 2개 이상의 덩어리인지 확인
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if check_melted == True and tmp[i][j] >= 1:
                check_melted = False

            if tmp[i][j] >= 1 and visit[i][j] == 0:
                # 하나의 덩어리가 발견된 이후에 if 문에 걸렸다면 덩어리가 2개
                if check_num == 1:
                    check_num += 1
                    break

                dfs(i, j)
                check_num = 1  # 덩어리 개수: 1

        if check_num == 2:
            break

    # 빙산이 두 덩어리 이상 존재하므로 while 문 break 후, year 출력
    if check_num == 2:
        break

    # 빙산이 모두 녹을 때까지 분리되지 않았다면 0 출력
    if len(ice) == 0:
        print(0)
        exit()

    # 빙산이 두 덩어리 이상 존재하지 않으므로 빙산 녹이기
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            cnt = 0
            if tmp[i][j] >= 1:
                # 상하좌우로 바닷물에 접해있는 방향 카운트
                for x, y in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                    if tmp[x][y] == 0:
                        cnt += 1

                if tmp[i][j] <= cnt:
                    tmp[i][j] = 0
                else:
                    tmp[i][j] = tmp[i][j] - cnt

    year += 1

    # for i in range(n):
    #     for j in range(m):
    #         print(tmp[idx1][i][j], end=" ")
    #     print()

    ice = copy.deepcopy(tmp)

print(year)
