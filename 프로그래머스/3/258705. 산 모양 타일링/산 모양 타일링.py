def solution(n, tops):
    rest = [0] * (n + 1)
    right = [0] * (n + 1)

    rest[0], right[0] = 1, 0

    for i in range(1, n + 1):
        if tops[i-1]:
            rest[i] = (rest[i - 1] * 3 + right[i - 1] * 2) % 10007
            right[i] = (rest[i - 1] + right[i - 1]) % 10007
        else:
            rest[i] = (rest[i - 1] * 2 + right[i - 1]) % 10007
            right[i] = (rest[i - 1] + right[i - 1]) % 10007

    return (rest[n] + right[n]) % 10007
