from collections import deque

n,m=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

queue=deque([])
cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            queue.append((i,j))
        elif graph[i][j]==0:
            cnt+=1

while queue:
    x,y=queue.popleft()
    

