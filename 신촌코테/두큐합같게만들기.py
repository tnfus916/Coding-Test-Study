from collections import deque


def solution(queue1, queue2):
    def get_idx(idx):
        if idx == len(queue):
            return 0
        else:
            return idx

    queue = deque(queue1 + queue2)

    idx1 = 0
    idx2 = len(queue1)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 두 수의 합이 홀수일 때
    if (sum1 + sum2) % 2 != 0:
        return -1

    cnt = 0
    while True:
        if sum1 > sum2:
            if idx2 - idx1 == 1 or idx2 - idx1 + len(queue) == 1:
                return -1

            sum1 -= queue[idx1]
            sum2 += queue[idx1]
            idx1 = get_idx(idx1 + 1)

            cnt += 1

        elif sum1 < sum2:
            if idx1 - idx2 == 1 or idx1 - idx2 + len(queue) == 1:
                return -1

            sum1 += queue[idx2]
            sum2 -= queue[idx2]
            idx2 = get_idx(idx2 + 1)

            cnt += 1
        else:
            return cnt


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))


# from collections import deque


# def solution(queue1, queue2):
#     queue1 = deque(queue1)
#     queue2 = deque(queue2)

#     sum1 = sum(queue1)
#     sum2 = sum(queue2)

#     # 두 수의 합이 홀수일 때
#     if (sum1 + sum2) % 2 != 0:
#         return -1

#     cnt = 0
#     while True:
#         if sum1 > sum2:
#             if len(queue1) == 1:
#                 return -1
#             num = queue1.popleft()
#             queue2.append(num)
#             sum1 -= num
#             sum2 += num
#             cnt += 1
#         elif sum1 < sum2:
#             if len(queue2) == 1:
#                 return -1
#             num = queue2.popleft()
#             queue1.append(num)
#             sum1 += num
#             sum2 -= num
#             cnt += 1
#         else:
#             return cnt
