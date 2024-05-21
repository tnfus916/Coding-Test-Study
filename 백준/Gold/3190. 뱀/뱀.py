import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

l = int(input())
time = {}
for _ in range(l):
    x, c = map(str, input().split())
    x = int(x)
    time[x] = c

dirc = 0  # 0, 1, 2, 3 = 오, 아래, 왼, 위
t = 0
snake = deque([(0, 0)])
while True:
    t += 1

    if dirc == 0:
        x, y = snake[-1][0], snake[-1][1] + 1
    elif dirc == 1:
        x, y = snake[-1][0] + 1, snake[-1][1]
    elif dirc == 2:
        x, y = snake[-1][0], snake[-1][1] - 1
    else:
        x, y = snake[-1][0] - 1, snake[-1][1]

    if x < 0 or x >= n or y < 0 or y >= n:
        print(t)
        break

    if (x, y) in snake:
        print(t)
        break

    if graph[x][y] == 1:
        snake.append((x, y))
        graph[x][y] = 0
    elif graph[x][y] == 0:
        snake.popleft()
        snake.append((x, y))

    if t in time:
        if time[t] == "D":
            dirc = (dirc + 1) % 4
        elif time[t] == "L":
            dirc = (dirc - 1) % 4
