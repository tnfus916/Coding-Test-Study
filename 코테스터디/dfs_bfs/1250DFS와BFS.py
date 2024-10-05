from collections import deque
import sys
input=sys.stdin.readline

def dfs(srt):
    visit[srt]=1
    print(srt+1,end=' ')
    for i in graph[srt]:
        if visit[i]==0:
            dfs(i)
    return 

def bfs(srt):
    queue=deque([srt])
    visit[srt]=1
    while queue:
        curr=queue.popleft()
        print(curr+1,end=' ')
        for i in graph[curr]:
            if visit[i]==0:
                visit[i]=1
                queue.append(i)
    return 

node,edge,srt=map(int,input().split())
graph=[[] for _ in range(node)]
for _ in range(edge):
    n1,n2=map(int,input().split())
    if n1-1 not in graph[n1-1]:
        graph[n1-1].append(n2-1)
    if n2-1 not in graph[n2-1]:
        graph[n2-1].append(n1-1)

for i in range(node):
    graph[i].sort()

visit=[0]*node
dfs(srt-1)
print()

visit=[0]*node
bfs(srt-1)
