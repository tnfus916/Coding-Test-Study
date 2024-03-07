import math


def solution(n, k):
    def find_prime(p):
        for i in range(2, int(math.sqrt(p)) + 1):
            if p % i == 0:
                return False

        return True

    answer = 0

    # k진수로 변환
    num = ""
    while n > 0:
        num = str(n % k) + num
        n //= k

    arr = num.split("0")

    # 소수찾기
    for i in arr:
        if i == "" or i == "1":
            continue

        if find_prime(int(i)):
            answer += 1

    return answer


