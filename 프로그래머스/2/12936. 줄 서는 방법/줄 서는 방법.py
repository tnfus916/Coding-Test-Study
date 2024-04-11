from functools import reduce
import math

def solution(n, k):
    answer = []
    tmp = [i + 1 for i in range(n)]

    i = 1
    case = reduce(lambda x,y:x*y,range(1,n))
    while i < n:
        if k==0:
            tmp.sort(reverse=True)
            answer+=tmp
            break
        if k==1:
            answer+=tmp
            break
        
        idx = math.ceil(k/case)-1
        answer.append(tmp[idx])
        tmp.pop(idx)
        
        
        k %= case
        case //= n-i
        i += 1
        
    return answer
