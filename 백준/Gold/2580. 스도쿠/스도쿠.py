import sys

input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]


def check_hor(x, num):
    for i in range(9):
        if num == sudoku[x][i]:
            return False
    return True


def check_ver(y, num):
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    return True


def check_box(x, y, num):
    a = x // 3 * 3
    b = y // 3 * 3
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if num == sudoku[i][j]:
                return False
    return True


def dfs(idx):
    # 빈칸을 다 메꿨으면 결과값 출력
    if idx == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit()

    for n in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if check_hor(x, n) and check_ver(y, n) and check_box(x, y, n):
            sudoku[x][y] = n
            dfs(idx + 1)
            sudoku[x][y] = 0


blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

idx = 0
dfs(idx)
