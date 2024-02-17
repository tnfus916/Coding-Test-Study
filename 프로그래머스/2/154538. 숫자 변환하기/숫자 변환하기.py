from collections import deque

def solution(x, y, n):
    answer = 0
    
    queue=deque([(x,0)])  
    visited=[0]*(y+1)
    visited[x]=1
    while queue:
        num,cnt=queue.popleft()
        if num==y:
            return cnt 
        
        for next_num in [num+n,num*2,num*3]:
            if next_num<=y and visited[next_num]==0:
                visited[next_num]=1
                queue.append((next_num,cnt+1))
    
    return -1