def solution(board, skill):
    answer = 0
    for [typ, r1, c1, r2, c2, degree] in skill:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if typ == 1:
                    board[i][j] -= degree
                elif typ == 2:
                    board[i][j] += degree

    for i in range(len(board)):
        for j in range(len(board[-1])):
            if board[i][j] >= 1:
                answer += 1

    return answer


def solution(board, skill):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[-1])):
            tmp = board[i][j]
            for [typ, r1, c1, r2, c2, degree] in skill:
                if r1 <= i <= r2 and c1 <= j <= c2:
                    if typ == 1:
                        tmp -= degree
                    else:
                        tmp += degree
            if tmp >= 1:
                answer += 1

    return answer


def solution(board, skill):
    answer = 0

    r = len(board)
    c = len(board[0])

    tmp = [[0] * (c + 1) for _ in range(r + 1)]
    for typ, r1, r2, c1, c2, degree in skill:
        if typ == 1:
            degree = -degree

        tmp[r1][c1] += degree
        tmp[r2 + 1][c1] -= degree
        tmp[r1][c2 + 1] -= degree
        tmp[r2 + 1][c2 + 1] += degree

    for i in range(r):
        for j in range(1, c):
            tmp[i][j] += tmp[i][j - 1]

    for j in range(c):
        for i in range(1, r):
            tmp[i][j] += tmp[i - 1][j]

    for i in range(r):
        for j in range(c):
            if board + tmp[i][j] >= 1:
                answer += 1

    return answer
