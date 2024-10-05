d,k=map(int,input().split())

dp=[(0,0),(1,0),(0,1)] # 첫날 (A,0), 둘째날 (0,B)

# 셋째날 (A+0,0+B)=>(A,B), 넷째날 (0+A,B+B)=>(A,2B)
for i in range(3,d+1):
    dp.append((dp[i-2][0]+dp[i-1][0],dp[i-2][1]+dp[i-1][1]))

a=dp[-1][0] # A의 계수
b=dp[-1][1] # B의 계수

# 가장 큰 B값부터 시작해서 A, B 추측
max_b=k//b
for i in range(max_b,0,-1):
    if (k-b*i)%a==0:
        A=(k-b*i)//a
        if A==0:
            continue
        B=i
        break
print(A)
print(B)
        




