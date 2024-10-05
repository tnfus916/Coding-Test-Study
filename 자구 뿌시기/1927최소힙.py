import sys

def heap_pop(heap):
    if len(heap)==0:
        print(0)
        return 
    elif len(heap)==1:
        print(heap.pop())
        return 

    pop_item=heap[0]
    print(pop_item)
    heap[0]=heap.pop()
    now=0
    while now<len(heap):
        child=now*2+1
        if child+1<len(heap) and heap[child]>heap[child+1]:
            child+=1

        if child<len(heap) and heap[now]>heap[child]:
            heap[now],heap[child]=heap[child],heap[now]
            now=child
        else:
            break


def heap_push(heap,x):
    heap.append(x)
    now=len(heap)-1
    while now>0:
        par=(now-1)//2
        if heap[par]>heap[now]:
            heap[par],heap[now]=heap[now],heap[par]
            now=par
        else:
            break




n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        heap_pop(heap)
    elif x>0:
        heap_push(heap,x)