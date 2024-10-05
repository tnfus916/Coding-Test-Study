from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def dfs(i):
    visit[i]=1
    for j in range(n):
        if graph[i][j]==1:
            dfs(j)


for i in range(n):
    visit=[0]*n
    dfs(i)
    
    # queue=deque([])
    # for j in range(n):
    #     if graph[i][j]==1:
    #         queue.append(j)
    # while queue:
    #     node=queue.popleft()
    #     for k in range(n):
    #         if graph[node][k]==1 and graph[i][k]==0:
    #             graph[i][k]=1
    #             queue.append(k)

for i in range(n):
    for j in range(n):
        print(graph[i][j],end=" ")
    print()

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j]==1:
                    continue
                if graph[i][k]==1 and graph[k][j]==1:
                    graph[i][j]=1
                    
    for i in range(n):
        for j in range(n):
            print(graph[i][j],end=' ')              
        print()
