import sys

def heap_pop(heap):
    if len(heap)==0:
        print(0)
        return
    elif len(heap)==1:
        print(heap.pop())
        return

    pop_data=heap[0]
    print(pop_data)
    heap[0]=heap.pop()
    curr=0
    while curr<len(heap):
        child=curr*2+1
        if child+1<len(heap) and heap[child]<heap[child+1]:
            child+=1
        
        if child<len(heap) and heap[curr]<heap[child]:
            heap[curr],heap[child]=heap[child],heap[curr]
            curr=child
        else:
            break



def heap_push(heap,x):
    heap.append(x)
    curr=len(heap)-1
    while curr>0:
        parent=(curr-1)//2
        if heap[parent]<heap[curr]:
            heap[parent],heap[curr]=heap[curr],heap[parent]
            curr=parent
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

