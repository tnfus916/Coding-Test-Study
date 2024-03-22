import math


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        tmp = int(num != 1)

        # 나누어 떨어지는 값 중 가장 작은 수로 나눈 값 반환
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if num//i<=10**7:
                    tmp=max(tmp,num//i)
                    break
                if i<=10**7:
                    tmp=max(tmp,i)
                    
        answer.append(tmp)

    return answer
