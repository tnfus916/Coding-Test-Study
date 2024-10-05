# import copy


# def solution(n, info):
#     def get_dif(check, max_score):
#         nonlocal result
#         # 승부에 따른 점수의 차 구하기
#         score = 0
#         for i in range(11):
#             if info[i] < check[i]:
#                 score += 10 - i
#             elif info[i] >= check[i] and info[i] != 0:
#                 score -= 10 - i

#         # 최대 점수 차, 라이언의 화살 조합 저장
#         if score > max_score:
#             max_score = score
#             # 화살 조합 저장
#             result = copy.deepcopy(check)

#             print("최대 점수차 갱신", max_score, result)

#         elif score == max_score:
#             # 이전에 구한 화살 조합과 비교
#             for i in range(10, -1, -1):
#                 if result[i] > check[i]:
#                     result = copy.deepcopy(check)
#                     return max_score
#             print("같은 최대 점수차", max_score, result)

#         return max_score

#     def dfs(idx):
#         nonlocal arrow
#         nonlocal max_score

#         if idx > 10 or arrow > n:
#             return

#         # (10-idx)점짜리 과녁에 화살 ryan[idx]번 쏜 경우 추가
#         arrow += ryan[idx]
#         check[idx] = ryan[idx]
#         print("전", idx, check)

#         if arrow == n:  # n개의 화살수를 다 채웠다면 최대 점수차 구하기
#             max_score = get_dif(check, max_score)

#             # 해제
#             arrow -= ryan[idx]
#             check[idx] = 0
#             print("후", idx, check)

#             dfs(idx + 1)

#         dfs(idx + 1)

#     arrow = 0
#     max_score = 0
#     ryan = [i + 1 for i in info]
#     check = [0] * 11
#     result = [0] * 11
#     dfs(0)

#     return result


# print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))


def solution(n, info):
    global max_gap, answer

    answer = [-1]
    score = [0] * 11
    max_gap = 0

    def is_winner_with_gap(score):
        a = 0  # 어피치 점수
        b = 0  # 라이언 점수

        for i in range(len(info)):
            if info[i] > 0 or score[i] > 0:
                if info[i] >= score[i]:
                    a += 10 - i
                else:
                    b += 10 - i
        return (b > a, abs(a - b))

    def dfs(L, cnt):
        global max_gap, answer
        if L == 11 or cnt == 0:
            is_winner, gap = is_winner_with_gap(score)
            if is_winner:
                if cnt >= 0:  # 화살이 남은 경우
                    score[10] = cnt  # 0점에 쏴도 이김

                if gap > max_gap:  # 갭이 더 큰 경우로 업데이트
                    max_gap = gap
                    answer = score.copy()

                elif gap == max_gap:  # 가장 낮은 점수를 많이 맞힌 경우로 업데이트
                    for i in range(len(score)):
                        if answer[i] > 0:
                            max_i_1 = i
                        if score[i] > 0:
                            max_i_2 = i
                    if max_i_2 > max_i_1:
                        answer = score.copy()

            return

        # k점을 어피치보다 많이 맞추거나 아예 안맞추거나
        if cnt > info[L]:  # 어피치가 L 과녁에 쏜 화살보다 남은 화살의 개수가 크면
            score[L] = info[L] + 1
            dfs(L + 1, cnt - (info[L] + 1))
            score[L] = 0

        # L 과녁에 어피치보다 더 많이 쏠 수 없다면 패스
        dfs(L + 1, cnt)

    dfs(0, n)

    return answer
