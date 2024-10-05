n = int(input())

table = []
for _ in range(n):
    day, price = map(int, input().split())
    table.append((day, price))

dp = [0] * (n + 1)
dp = [0 for i in range(n + 1)]
# 이 둘의 차이

# for i in range(n):
#     for j in range(i+table[i][0],n+1):
#         if dp[j]<dp[i]+table[i][1]:
#             dp[j]=dp[i]+table[i][1]

# print(dp[-1])

# for i in range(n-1,-1,-1):
#     day=table[i][0]
#     price=table[i][1]

#     if i==n-1:
#         if day==1:
#             dp[i]=price
#         continue

#     if day>n-i:
#         continue
#     elif day==n-i:
#         dp[i]=price
#     else:
#         dp[i]=price+max(dp[i+day:])
