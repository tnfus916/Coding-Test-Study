def solution(participant, completion):
    answer = ''
    
    dic={}
    for com in completion:
        if com not in dic:
            dic[com]=1
        else:
            dic[com]+=1
    
    for par in participant:
        if par not in dic:
            return par
        else:
            dic[par]-=1
            if dic[par]==0:
                dic.pop(par)
                
    return answer