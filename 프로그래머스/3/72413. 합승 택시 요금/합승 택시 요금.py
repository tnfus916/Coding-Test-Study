

def solution(n, s, a, b, fares):
    answer = 0
    
    graph=[[10**9]*(n+1) for _ in range(n+1)]
    for c,d,f in fares:
        graph[c][d]=f
        graph[d][c]=f
    
    for i in range(1,n+1):
        graph[i][i]=0
        
    # 플로이드 와샬
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if graph[i][k]+graph[k][j]<graph[i][j]:
                    graph[i][j]=graph[i][k]+graph[k][j]
                    graph[j][i]=graph[i][k]+graph[k][j]
    
    answer=graph[s][a]+graph[s][b]
    for i in range(1,n+1):
        answer=min(answer,graph[s][i]+graph[i][b]+graph[i][a])
        
    return answer