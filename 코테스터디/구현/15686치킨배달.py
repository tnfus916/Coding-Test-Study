from collections import deque
def bfs(x,y):
    queue=deque([(x,y,0)])
    tmp=city
    tmp[x][y]=3
    cnt=0
    breakcheck=0
    while queue:
        for a,b in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if a>=0 and a<n and b>=0 and b<n and tmp[a][b]>0:
                if city[a][b]==2: # 치킨 찾으면 bfs 끝. 
                    cnt+=1
                    breakcheck=1
                    break
                tmp[a][b]=-1 # visit표시 
                queue.append(a,b,cnt+1)
        if breakcheck==1:
            break
    return cnt,a,b
    



n,m=map(int,input().split())

city=[]
for _ in range(n):
    city.append(list(map(int,input().split())))

kfc={}

for i in range(n):
    for j in range(n):
        if city[i][j]==1:
            # cnt,a,b=bfs(i,j)
            if (i,j) not in kfc:
                kfc[(i,j)]=[bfs(i,j)]
            else:
                kfc[(i,j)].append(bfs(i,j))