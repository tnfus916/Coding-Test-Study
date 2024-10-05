from collections import deque

case=int(input())
for _ in range(case):
    n=int(input())
    srtX,srtY=map(int,input().split())
    destX,destY=map(int,input().split())

    visit=[[0]*n for _ in range(n)]
    queue=deque([(srtX,srtY,0)])
    visit[srtX][srtY]=1
    while queue:
        curX,curY,cnt=queue.popleft()
        if curX==destX and curY==destY:
            print(cnt)
            break
        for i,j in [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]:
            if curX+i>=0 and curX+i<n and curY+j>=0 and curY+j<n:
                if visit[curX+i][curY+j]==0:
                    visit[curX+i][curY+j]=1
                    queue.append((curX+i,curY+j,cnt+1))