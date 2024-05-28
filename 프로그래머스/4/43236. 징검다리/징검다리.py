def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks=[0]+rocks+[distance]
    
    srt, end=1,distance
    while srt<=end:
        mid=(srt+end)//2
        
        prev,cnt=0,0
        for i in range(1,len(rocks)):
            if cnt>n:
                break
                
            if rocks[i]-prev>=mid:
                prev=rocks[i]
            else:
                cnt+=1
        
        if cnt>n:
            end=mid-1
        else:
            answer=mid
            srt=mid+1
            
    return answer