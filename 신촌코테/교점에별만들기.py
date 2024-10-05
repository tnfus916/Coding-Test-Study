def solution(line):
    # 교점 구하기
    leng = len(line)
    meet_x = []
    meet_y = []
    for i in range(leng):
        a, b, e = line[i]
        for j in range(i + 1, leng):
            c, d, f = line[j]

            # 두 직선이 평행 또는 일치
            if a * d - b * c == 0:
                continue

            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x == int(x) and y == int(y):
                meet_x.append(int(x))
                meet_y.append(int(y))

    # 그래프 크기 정하기
    height = max(meet_x) - min(meet_x)
    width = max(meet_y) - min(meet_y)
    graph = [["."] * width for _ in range(height)]

    # 좌표 변환하여 그래프에 별 표시하기
    srt_x, srt_y = min(meet_x), max(meet_y)  # 출력값의 좌측 상단 좌표
    for i in range(len(meet_x)):
        new_x = srt_y - meet_y[i]
        new_y = meet_x[i] - srt_x
        print(new_x, new_y)
        graph[new_x][new_y] = "*"

    print(graph)

    return
