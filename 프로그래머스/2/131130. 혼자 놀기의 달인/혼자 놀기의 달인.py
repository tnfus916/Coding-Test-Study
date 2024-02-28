def solution(cards):
    def check_box(num):
        nonlocal v

        if visit[num] == v:
            return

        if visit[num] == -1:
            visit[num] = v
            check_box(cards[num] - 1)

    visit = [-1] * len(cards)
    v = 0
    for card in cards:
        if visit[card - 1] == -1:
            check_box(card - 1)
            v += 1

    # 각 visit 그룹별로 가장 개수가 많은 2개 세기
    if v==1:
        return 0 
    
    cnt = [0] * v
    for vi in visit:
        cnt[vi] += 1

    cnt.sort(reverse=True)

    answer = cnt[0] * cnt[1]

    return answer
