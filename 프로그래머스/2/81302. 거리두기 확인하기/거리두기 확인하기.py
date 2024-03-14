def solution(places):
    answer = []

    def check_next(x, y, idx):
        for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= a < 5 and 0 <= b < 5 and places[idx][a][b] == "P":
                return True
        return False

    def check_over(x, y, idx):
        cnt = 0
        for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= a < 5 and 0 <= b < 5 and places[idx][a][b] == "P":
                cnt += 1

        if cnt >= 2:
            return True
        return False

    for idx, place in enumerate(places):
        breakcheck = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P" and check_next(i, j, idx):
                    breakcheck = 1
                    break

                elif place[i][j] == "O" and check_over(i, j, idx):
                    breakcheck = 1
                    break

            if breakcheck == 1:
                break

        if breakcheck == 1:
            answer.append(0)
        else:
            answer.append(1)

    return answer
