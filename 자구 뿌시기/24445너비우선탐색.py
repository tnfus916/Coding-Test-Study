import sys
from collections import deque

n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

queue=deque([r-1])
visit=[0]*n
visit[r-1]=1
seq=[0]*n
cnt=1

while True:
    if len(queue)==0:
        break
    now=queue.popleft()
    seq[now]=cnt
    cnt+=1
    graph[now].sort(reverse=True)

    for node in graph[now]:
        if visit[node]==0:
            visit[node]=1
            queue.append(node)

for ans in seq:
    print(ans)
