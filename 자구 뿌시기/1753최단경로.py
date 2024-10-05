import heapq
import sys
input=sys.stdin.readline

v,e=map(int,input().split())
srt=int(input())-1

graph=[[] for _ in range(v)]
for _ in range(e):
    a,b,c=map(int,input().split())
    graph[a-1].append([c,b-1])

dist=[10**9]*v
dist[srt]=0
heap=[]
heapq.heappush(heap,[0,srt])
while heap:
    weight,fromm=heapq.heappop(heap)
    for w, to in graph[fromm]:
        if dist[to]>weight+w:
            dist[to]=weight+w
            heapq.heappush(heap,[weight+w,to])
            
for ans in dist:
    if ans>=10**9:
        print('INF')
    else:
        print(ans)