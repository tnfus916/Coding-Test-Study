import heapq
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
graph=[[] for _ in range(v)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append([c,b-1])
    graph[b-1].append([c,a-1])

visit=[0]*v
heap=[]
ans=0

heapq.heappush(heap,[0,0])
while heap:
    weight,fromm=heapq.heappop(heap)
    if visit[fromm]==1:
        continue
    visit[fromm]=1
    ans+=weight

    for w,to in graph[fromm]:
        if visit[to]==0:
            heapq.heappush(heap,[w,to])
            
print(ans)