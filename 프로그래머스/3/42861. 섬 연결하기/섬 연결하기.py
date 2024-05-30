def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x:x[2])
    edge=set([costs[0][0]])
    
    while len(edge)!=n:
        for n1,n2,c in costs:
            if n1 in edge and n2 in edge:
                continue
            if n1 in edge or n2 in edge:
                edge.update([n1,n2])
                answer+=c
                break
                
    return answer