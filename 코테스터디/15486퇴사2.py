import sys
input=sys.stdin.readline

n=int(input())
consult=[(0,0)]
for _ in range(n):
    t,p=map(int,input().split()) 
    consult.append((t,p))

# 앞에서부터 bottom up
dp=[0]*(n+1)
for i in range(1,n+1):
    dp[i]=max(dp[i-1],dp[i]) # 전날까지의 최대 이익과 비교
    if i+consult[i][0]-1<=n:
        dp[i+consult[i][0]-1]=max(dp[i+consult[i][0]-1],dp[i-1]+consult[i][1])    
print(dp[-1])