def dfs(node):
    global cnt
    visit[node]=1
    for near in graph[node]: # 인접 리스트에서 인접 노드 찾기
        if visit[near]==0: # 방문한 적이 없는 노드라면 카운트, dfs 한칸 들어가기
            cnt+=1
            dfs(near)



com=int(input())   # 컴퓨터의 개수 입력
edge=int(input())  # 컴퓨터 간 연결 간선 입력 

# 인접 리스트 사용 
graph=[[] for _ in range(com+1)] 
for _ in range(edge):
    c1,c2=map(int,input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

visit=[0]*(com+1)
cnt=0

dfs(1)
print(cnt)