def solution(scores):
    # 완호의 점수 저장
    wanho = scores[0]
    summ = wanho[0] + wanho[1]

    # 근무태도점수, 동료평가점수가 큰 순으로 정렬
    scores.sort(key=lambda x: (x[0], x[1]), reverse=True)

    tmp = scores[0][1]
    max_peer = tmp
    result = [scores[0][0] + scores[0][1]]
    for i in range(1, len(scores)):
        if wanho[0] < scores[i][0] and wanho[1] < scores[i][1]:
            return -1

        # 근무태도점수가 달라질 때 == 줄었을 때
        if scores[i][0] != scores[i - 1][0]:
            max_peer = tmp
            tmp = scores[i][1]

        # 동료평가점수가 max_peer보다 같거나 크면 인센티브 o
        if scores[i][1] >= max_peer:
            result.append(scores[i][0] + scores[i][1])

        i += 1

    # 등수 매기기
    result.sort(reverse=True)
    idx = result.index(summ)

    return idx + 1


print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]))
# def solution(scores):
#     target = scores[0]
#     summ = target[0] + target[1]

#     # 인센티브 받는 사원 필터링
#     scores.sort(key=lambda x: (x[0], x[1]), reverse=True)

#     max_peer = scores[0][1]
#     i = 1
#     while i < len(scores):
#         if scores[i][0] != scores[i - 1][0]:
#             max_peer = max(max_peer, scores[i][1])

#         if scores[i][1] < max_peer:
#             # 완호가 인센티브를 받지 못할 때
#             if scores[i] == target:
#                 return -1

#             scores.pop(i)
#             continue

#         i += 1

#         # # 근무태도점수가 달라질 때 == 줄었을 때
#         # if scores[i][0] != scores[i - 1][0]:
#         #     max_peer=tmp
#         #     tmp=scores[i][1]

#         # # 동료평가점수가 max_peer보다 낮으면 인센티브 x
#         # if scores[i][1] < max_peer:
#         #     # 완호가 인센티브를 받지 못할 때
#         #     if scores[i] == wanho:
#         #         return -1

#         #     scores.pop(i)
#         #     continue

#         # i += 1

#     # 등수 매기기
#     result = []
#     for i in range(len(scores)):
#         result.append(scores[i][0] + scores[i][1])
#     result.sort(reverse=True)

#     idx = result.index(summ)
#     return idx + 1
