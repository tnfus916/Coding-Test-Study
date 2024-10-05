from collections import deque

n,m=map(int,input().split())
pop_arr=list(map(int,input().split()))

queue=deque([i+1 for i in range(n)])
cur=0

ans=0
for num in pop_arr:
    idx=queue.index(num)
    move_cnt=min(abs(cur-idx),len(queue)-abs(cur-idx))
    ans+=move_cnt
    queue.remove(num)
    cur=idx
print(ans)




