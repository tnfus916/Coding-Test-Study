import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[10**6]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    if graph[a-1][b-1] >c:
        graph[a-1][b-1]=c

for i in range(n):
    graph[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j: continue
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j]>10**6:
            print(0, end=' ')
        else:
            print(graph[i][j],end=' ')
    print()