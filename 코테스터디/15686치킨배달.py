from itertools import combinations

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

# 기존 치킨집의 좌표 저장 후 빈 공간으로 설정, 일반집의 좌표도 저장 
chicken=[]
house=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==2:
            chicken.append((i,j))
            graph[i][j]=0
        elif graph[i][j]==1:
            house.append((i,j))

# m개의 치킨 집을 선택한 후 치킨 집으로 표시, 각 집에서 치킨 집까지의 거리 계산하여 최소 도시의 치킨 거리 구하기  
ans=10**9
for new_chicken in list(combinations(chicken,m)):
    for x,y in new_chicken:
        graph[x][y]=2
    
    cnt=0
    for x,y in house:
        #Zz
    ans=min(ans,cnt)

    for x,y in new_chicken:
        graph[x][y]=0
    
print(ans)

