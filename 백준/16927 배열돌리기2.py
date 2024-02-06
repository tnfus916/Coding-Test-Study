import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# graph에 각 링의 값들을 시계방향으로 넣기
ring = min(n, m) // 2  # 링의 개수
graph = [[] for _ in range(ring)]  # 각 링의 값들을 하나의 1차원 배열에 저장
result = [[0] * m for _ in range(n)]  # 결과값 저장
for i in range(ring):
    x = i
    y = i  # 각 링의 시작점

    a = n - 2 * i
    b = m - 2 * i  # 각 링들의 세로 가로 길이

    # 하나의 링들의 값을 1차원 배열에 저장
    graph[i].append(arr[x][y])
    dirct = "right"

    for _ in range(2 * (a + b) - 4 - 1):
        if x == i and y == i + b - 1:  # 가장 오른쪽 상단에 도달하면 아래로
            dirct = "down"
        elif x == i + a - 1 and y == i + b - 1:  # 오른쪽 하단에 도달하면 왼쪽으로
            dirct = "left"
        elif x == i + a - 1 and y == i:  # 왼쪽 하단에 도달하면 위로
            dirct = "up"

        if dirct == "right":
            y += 1
        elif dirct == "down":
            x += 1
        elif dirct == "left":
            y -= 1
        elif dirct == "up":
            x -= 1

        graph[i].append(arr[x][y])

    # 회전시키고 result에 담기
    x = i
    y = i
    dirct = "right"
    rotate = r % (a * b) + 1
    idx = rotate  # 회전수를 graph 배열의 인덱스로 사용
    for _ in range(2 * (a + b) - 4):
        if x == i and y == i + b - 1:
            dirct = "down"
        elif x == i + a - 1 and y == i + b - 1:
            dirct = "left"
        elif x == i + a - 1 and y == i:
            dirct = "up"

        if dirct == "right":
            y += 1
        elif dirct == "down":
            x += 1
        elif dirct == "left":
            y -= 1
        elif dirct == "up":
            x -= 1

        if idx >= 2 * (a + b) - 4:  # 링의 길이보다 커지면 0으로 할당
            idx = 0

        result[x][y] = graph[i][idx]
        idx += 1

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()
