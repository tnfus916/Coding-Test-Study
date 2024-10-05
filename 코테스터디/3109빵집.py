def dfs(row, col):
    global r, c, cnt
    graph[row][col] = "x"

    # print(row, col)
    # for i in range(r):
    #     for j in range(c):
    #         print(graph[i][j], end=" ")
    #     print()

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


# r, c = map(int, input().split())

# graph = [list(map(str, " ".join(input()).split())) for _ in range(r)]
# visit = [[0] * c for _ in range(r)]

# row = 0
# cnt = 0
# for row in range(r):
#     col = 0
#     breakcheck = 0
#     while col < c - 1:
#         print(row, col)
#         for i in range(r):
#             for j in range(c):
#                 print(graph[i][j], end=" ")
#             print()

#         if row - 1 >= 0 and graph[row - 1][col + 1] == ".":
#             graph[row - 1][col + 1] = "x"
#             row -= 1
#         elif graph[row][col + 1] == "." and visit[row][col + 1] == 0:
#             graph[row][col + 1] = "x"
#         elif row + 1 < r and graph[row + 1][col + 1] == ".":
#             graph[row + 1][col + 1] = "x"
#             row += 1
#         else:
#             breakcheck = 1
#             break

#         col += 1

#     if breakcheck == 0:
#         cnt += 1

# print(cnt)
