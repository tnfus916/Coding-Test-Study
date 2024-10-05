from collections import deque 
n=int(input())
# 동일 자리수 input
arr=list(map(int,input().split()))
bucket=[deque() for _ in range(10)]

num=arr[0]
leng=0
while True:
    if num<=0:
        break
    num//=10
    leng+=1
    
queue=deque(arr)
for i in range(leng):
    while queue: 
        num=queue.popleft()
        bucket[(num//(10**i))%10].append(num)
    for deq in bucket:
        while deq:
            queue.append(deq.popleft())
print(list(queue))