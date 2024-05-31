def solution(routes):
    answer = 0
    
    routes.sort(key=lambda x:x[1])
    
    prev=-30001
    cnt=0
    for route in routes:
        if route[0] > prev:
            cnt += 1
            prev = route[1]
            
    return cnt
    

