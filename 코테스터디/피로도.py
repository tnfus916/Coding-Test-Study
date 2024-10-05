from itertools import permutations

def solution(k, dungeons):
    
    # 탐험할 수 있는 최대 던전 수 탐색
    for p in permutations(dungeons,len(dungeons)):
        now = k
        cnt = 0
        for needed, useup in dungeons:
            if now >= needed:
                now = now - useup 
                cnt += 1
        answer = max(answer, cnt)
    
    return answer

arr=[[80,20],[50,40],[30,10],[79,10],[61,20]]
print(solution(80,arr))