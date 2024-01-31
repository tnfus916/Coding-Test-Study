def dfs(row, col):
    global r, c, cnt
    graph[row][col] = "x"

    if col == c - 1:
        cnt += 1
        return True

    y = col + 1
    for x in [row - 1, row, row + 1]:
        if x >= 0 and x < r and y >= 0 and y < c and graph[x][y] == ".":
            graph[x][y] = "x"
            if dfs(x, y):
                return True

    return False


r, c = map(int, input().split())
graph = [list(map(str, input().rstrip())) for _ in range(r)]

cnt = 0
for i in range(r):
    dfs(i, 0)

print(cnt)
