def solution(x, y, n):
    dp=[-1]*1000001
    dp[x]=0
    
    if x==y:
        return 0
    
    for i in range(x,y+1):
        if dp[i]==-1:
            continue
        
        for near in [i+n,i*2,i*3]:
            # 한번도 도달하지 않았던 숫자라면 이전 수의 연산 횟수에 +1
            if near<=y:
                if dp[near]==-1:
                    dp[near]=dp[i]+1
                else:
                    dp[near]=min(dp[near],dp[i]+1)
                
                # if near==y:
                #     i=near
                #     return dp[near]
                
    answer=dp[y]
    
    return answer