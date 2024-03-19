def solution(weights):
    answer = 0
    
    dic={}
    for w in weights:
        if w not in dic:
            dic[w]=1
        else:
            dic[w]+=1
    
    visit=[] # weights에 중복되는 몸무게가 있는 경우 방문 표시 
    for w in weights:
        if dic[w]>1 and w not in visit:
            visit.append(w)
            answer+=dic[w]*(dic[w]-1)//2
            
        if int(w/2)==w/2 and w/2 in dic:
            answer+=dic[w//2]
        if int(w*2/3)==w*2/3 and w*2/3 in dic:
            answer+=dic[w*2/3]
        if int(w*3/4)==w*3/4 and w*3/4 in dic:
            answer+=dic[w*3/4]
        
    return answer