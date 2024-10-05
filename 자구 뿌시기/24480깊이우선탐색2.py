import sys
sys.setrecursionlimit(10 ** 8)

def dfs(now):
    global cnt

    visit[now]=1
    seq[now]=cnt
    graph[now].sort(reverse=True)
    
    for node in graph[now]:
        if visit[node]==0:
            cnt+=1
            dfs(node)                

n,m,r=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visit=[0]*n
seq=[0]*n
cnt=1
dfs(r-1)

for ans in seq:
    print(ans)

