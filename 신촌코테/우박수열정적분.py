def solution(k, ranges):
    # 우박수열의 함수값과 1이 되는 x값 구하기
    x, y = 0, k
    graph = [k]
    while y != 1:
        if y % 2 == 0:
            y //= 2
        else:
            y = y * 3 + 1
        x += 1
        graph.append(y)
    n = x

    result = []
    for srt, end in ranges:
        # 구간의 시작점이 끝점보다 크다면 정적분 결과 -1로 반환
        if srt > end + n:
            result.append(-1)
            continue

        # 정적분
        summ = 0
        for i in range(srt, end + n):
            summ += (graph[i] + graph[i + 1]) // 2
        result.append(summ)

    return result
