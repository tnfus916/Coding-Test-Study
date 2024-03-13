def solution(picks, minerals):
    answer = 0

    # 곡괭이 수 x5 만큼 캘 수 있는 광물의 수만큼 minerals 리스트 자르기
    dia, iron, stone = picks
    pick_cnt = dia + iron + stone

    if pick_cnt * 5 < len(minerals):
        minerals = minerals[: pick_cnt * 5]

    # 광물 5개씩 묶기
    group = []
    tmp = [0, 0, 0]
    cnt = 0
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            tmp[0] += 1
        elif minerals[i] == "iron":
            tmp[1] += 1
        else:
            tmp[2] += 1

        cnt += 1

        if cnt == 5 or i == len(minerals) - 1:
            group.append(tmp)
            tmp = [0, 0, 0]
            cnt = 0

    # 피로도 계산
    group.sort(reverse=True)

    for idx in range(len(group)):
        d,i,s = group[idx]
        
        if idx < dia:
            answer += d + i + s
        elif idx < dia + iron:
            answer += d * 5 + i + s
        else:
            answer += d * 25 + i * 5 + s
        idx += 1

    return answer
