def solution(picks, minerals):
    answer = 0

    # (곡괭이 총합 x 5) 만큼 캘 수 있는 광물의 수만큼 minerals 리스트 자르기
    summ = sum(picks) * 5
    if summ < len(minerals):
        minerals = minerals[:summ]

    # 광물 5개씩 그룹으로 묶기
    group = []
    tmp = [0, 0, 0] # 묶음에서 [다이아,철,돌]의 개수
    cnt = 0
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            tmp[0] += 1
        elif minerals[i] == "iron":
            tmp[1] += 1
        else:
            tmp[2] += 1

        cnt += 1

        # 5개를 다 묶었거나, 마지막 묶음인데 5개보다 작을 때 group 배열에 추가 
        if cnt == 5 or i == len(minerals) - 1:
            group.append(tmp)
            tmp = [0, 0, 0]
            cnt = 0

    # 피로도 계산
    group.sort(reverse=True)

    dia, iron, stone = picks
    for idx in range(len(group)):
        d, i, s = group[idx]

        if idx < dia:
            answer += d + i + s
        elif idx < dia + iron:
            answer += d * 5 + i + s
        else:
            answer += d * 25 + i * 5 + s
        idx += 1

    return answer
