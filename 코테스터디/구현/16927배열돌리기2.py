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
    # 각 링의 시작점
    x = i
    y = i

    # 각 링들의 세로 가로 길이
    a = n - 2 * i
    b = m - 2 * i

    # 하나의 링들의 값을 1차원 배열에 저장(링의 길이: 2*(a+b)-4)
    for _ in range(2 * (a + b) - 4):
        # 꼭짓점에 도달했을 때 방향 바꿔주기
        if x == i and y == i:  # 왼쪽 상단
            dirct = "right"
        elif x == i and y == i + b - 1:  # 가장 오른쪽 상단
            dirct = "down"
        elif x == i + a - 1 and y == i + b - 1:  # 오른쪽 하단
            dirct = "left"
        elif x == i + a - 1 and y == i:  # 왼쪽 하단
            dirct = "up"

        graph[i].append(arr[x][y])

        # 방향에 따라 좌표값 이동시키기
        if dirct == "right":
            y += 1
        elif dirct == "down":
            x += 1
        elif dirct == "left":
            y -= 1
        elif dirct == "up":
            x -= 1

    # 1차원 배열에서 회전 시킨 후 result값에 저장
    rotate = r % (2 * (a + b) - 4)
    idx = rotate  # 회전수를 graph 배열의 인덱스로 사용

    x = i
    y = i
    for _ in range(2 * (a + b) - 4):
        # 꼭짓점에 도달했을 때 방향 바꿔주기
        if x == i and y == i:  # 왼쪽 상단
            dirct = "right"
        elif x == i and y == i + b - 1:  # 가장 오른쪽 상단
            dirct = "down"
        elif x == i + a - 1 and y == i + b - 1:  # 오른쪽 하단
            dirct = "left"
        elif x == i + a - 1 and y == i:  # 왼쪽 하단
            dirct = "up"

        result[x][y] = graph[i][idx]

        # 방향에 따라 좌표값 이동시키기
        if dirct == "right":
            y += 1
        elif dirct == "down":
            x += 1
        elif dirct == "left":
            y -= 1
        elif dirct == "up":
            x -= 1

        idx += 1

        # 링의 길이보다 커지면 0으로 할당
        if idx >= 2 * (a + b) - 4:
            idx = 0

for i in range(n):
    for j in range(m):
        print(result[i][j], end=" ")
    print()
