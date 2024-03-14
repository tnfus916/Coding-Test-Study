from collections import deque


def solution(n, m, x, y, r, c, k):
    answer = ""
    
    man=abs(x-r)+abs(y-c)
    
    # 맨하튼 거리와 홀짝이 같아야함 
    if man%2!=k%2:
        return "impossible"
    
    # k가 맨하튼 거리보다 작으면 안됨
    if k<man:
        return "impossible"
    
    dirc={(1,0):"d",(0,-1):"l",(0,1):"r",(-1,0):"u"}
    queue = deque([(x, y, 0, "")])
    while queue:
        i, j, cnt, path = queue.popleft()
        
        if (i, j) == (r, c) and (k-cnt) % 2:
            return 'impossible'

        if cnt == k and i == r and j == c:
                return path


        for di,dj in dirc:
            a=i+di
            b=j+dj
            if 1 <= a < n + 1 and 1 <= b < m + 1:
                if abs(a-r)+abs(b-c) + cnt >= k:
                    continue

                queue.append((a,b,cnt+1,path+dirc[(di,dj)]))
                break


