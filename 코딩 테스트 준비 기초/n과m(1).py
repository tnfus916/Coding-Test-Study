n,m=map(int,input().split())

arr=[]
visit=[0]*(n+1)
def count(cnt):
    if cnt==m:
        print(arr)
        return

    for i in range(1,n+1):
        if visit[i]==0:
            visit[i]=1
            arr.append(i)
            count(cnt+1)
            break
count(0)

# for문을 nCm*m*(m-1)*...*1