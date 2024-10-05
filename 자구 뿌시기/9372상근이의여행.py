import heapq
import sys
input=sys.stdin.readline

def get_cnt(now,cnt):
    visit[now]=1
    for node in graph[now]:
        if visit[node]==0:
            cnt=get_cnt(node,cnt+1)

    return cnt

test=int(input())
for _ in range(test):
    node,edge=map(int,input().split())
    visit=[0]*(node+1)
    graph=[[] for _ in range(node+1)]
    for _ in range(edge):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    cnt=get_cnt(1,0)

    # now=1
    # cnt=0
    # heap=[]
    # while cnt<node:
    #     visit[now]=1
    #     heapq.heappush(heap,now)
    #     for nodes in graph[now]:
    #         if visit[nodes]==0:
    #             heapq.heappush(heap,now)
    #     now=heapq.heappop()
    #     cnt+=1

    print(cnt)



