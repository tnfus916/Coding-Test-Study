def solution(today, terms, privacies):
    answer = []

    year, month, day = map(str, today.split("."))

    # 약관 종류 딕셔너리에 저장
    terms_d = {}
    for term in terms:
        term_type, term_month = term.split()
        terms_d[term_type] = int(term_month)

    for i in range(len(privacies)):
        date, typ = privacies[i].split()
        y, m, d = date.split(".")

        # 개월 수가 12가 넘어가면 년으로 변경
        dy, dm = divmod(int(m) + terms_d[typ], 12)
        if dm == 0:
            dy -= 1
            dm = 12
        y = int(y) + dy

        if dm < 10:
            dm = "0" + str(dm)

        expire_date = str(y) + str(dm) + str(d)
        today_date = year + month + day

        if expire_date <= today_date:
            answer.append(i + 1)

    return answer