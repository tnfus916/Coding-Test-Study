import heapq

def solution(N, road, K):
    answer = 0
    
    graph=[[10**9]*(N+1) for _ in range(N+1)]
    for srt,end,wght in road:
        graph[srt][end]=min(graph[srt][end],wght)
        graph[end][srt]=min(graph[end][srt],wght)
    
    heap=[(0,1)]
    dist=[10**9]*(N+1)
    dist[1]=0
    while heap:
        d,node=heapq.heappop(heap)
        
        if dist[node] <d:
            continue
        
        for near in range(1,N+1):
            w = graph[node][near]
            if w != 10**9:
                if d + w < dist[near]:
                    dist[near] = d + w
                heapq.heappush(heap,(d + w, near))
        
    for d in dist:
        if d<=K:
            answer+=1
            
    return answer