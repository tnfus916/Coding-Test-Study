import heapq

def solution(scoville, K):
    answer = 0
    
    heap=[]
    for food in scoville:
        heapq.heappush(heap,food)
        
    while heap:
        if heap[0]<K:
            if len(heap)>=2:
                f1=heapq.heappop(heap)
                f2=heapq.heappop(heap)
                heapq.heappush(heap,f1+2*f2)
                answer+=1
            elif len(heap)==1:
                return -1
        else:
            return answer