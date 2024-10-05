def solution(park, routes):
    h, w = len(park), len(park[0])

    def check(x, y, op, n):
        if op == "N":
            for i in range(1, n + 1):
                if x - i < 0 or park[x - i][y] == "X":
                    return False
        elif op == "S":
            for i in range(1, n + 1):
                if x + i >= h or park[x + i][y] == "X":
                    return False
        elif op == "W":
            for i in range(1, n + 1):
                if y - i < 0 or park[x][y - i] == "X":
                    return False
        elif op == "E":
            for i in range(1, n + 1):
                if y + i >= w or park[x][y + i] == "X":
                    return False

        return True

    # 시작점 찾기
    x, y = -1, -1
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                x, y = i, j
                break
        if x != -1 and y != -1:
            break

    # 경로 따라가기
    for r in routes:
        op, n = r.split()
        n = int(n)

        if check(x, y, op, n):
            if op == "N":
                x -= n
            elif op == "S":
                x += n
            elif op == "W":
                y -= n
            else:
                y += n

    return [x, y]
