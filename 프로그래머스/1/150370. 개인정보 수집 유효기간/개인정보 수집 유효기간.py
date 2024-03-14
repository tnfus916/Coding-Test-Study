def solution(today, terms, privacies):

    def cal_date(y, m, d, term):
        nonlocal year
        nonlocal month
        nonlocal day

        # 개월 수가 12가 넘어가면 년으로 변경
        dy, dm = divmod(m + term, 12)
        if dm == 0:
            dy -= 1
            dm = 12
        y += dy

        # # 1일일 때는 28일로, 나머지는 -1일
        # if d == 1:
        #     m -= 1
        #     d = 28
        # else:
        #     d -= 1
            
        # 오늘과 날짜 비교
        if y < year:
            return True

        if y==year and dm < month:
            return True

        if y==year and dm==month and d <= day:
            return True

        return False

    answer = []

    year, month, day = map(int, today.split("."))

    # 약관 종류 딕셔너리에 저장
    terms_d = {}
    for term in terms:
        t, m = map(str, term.split(" "))
        terms_d[t] = int(m)

    for i in range(len(privacies)):
        date, typ = map(str, privacies[i].split(" "))
        y, m, d = map(int, date.split("."))

        if cal_date(y, m, d, terms_d[typ]):
            answer.append(i + 1)

    return answer

