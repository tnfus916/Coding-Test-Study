import sys
input=sys.stdin.readline

n,l=map(int,input().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

ans=0
for i in range(n):
    flat=1
    downhill=0
    breakcheck=0
    slopecheck=[]
    for j in range(1,n):
        if graph[i][j-1]==graph[i][j]:
            flat+=1
            if downhill==1: # 이전에 만난 내리막을 내려오는중 
                if flat>=l: # 사다리를 놓을 수 있다면 
                    downhill=0 # 내리막 해결
                    slopecheck.append(j)

        else:
            if downhill==1: # 아직 내리막이 해결이 안됐는데 다른 경사로가 있다면 break
                breakcheck=1
                break
            if abs(graph[i][j-1]-graph[i][j])==1: # 칸 차이 1 
                if graph[i][j-1]<graph[i][j]: #오르막
                    if j-1 in slopecheck: 
                        breakcheck=1
                        break
                    if flat>=l:
                        flat=1 
                    else: # 경사로보다 사다리가 더 길어 break
                        breakcheck=1
                        break
                elif graph[i][j-1]>graph[i][j]: #내리막
                    flat=1
                    downhill=1
            else: # 칸 차이가 2 이상이니 x
                breakcheck=1
                break
    if breakcheck==0:
        print('i:',i)
        ans+=1

for j in range(n):
    flat=1
    downhill=0
    breakcheck=0
    for i in range(1,n):
        if graph[i-1][j]==graph[i][j]:
            flat+=1
            if downhill==1:
                if flat>=l:
                    downhill=0
        else:
            if downhill==1: # 아직 내리막이 해결이 안됐는데 다른 경사로가 있다면x
                breakcheck=1
                break
            if abs(graph[i-1][j]-graph[i][j])==1:
                if graph[i-1][j]<graph[i][j]: #오르막
                    if flat>=l:
                        flat=1 
                    else: # 경사로보다 사다리가 더 길어 설치 x
                        breakcheck=1
                        break
                elif graph[i-1][j]>graph[i][j]: #내리막
                    flat=1
                    downhill=1
            else: # 칸 차이가 2 이상이니 x
                breakcheck=1
                break
    if breakcheck==0:
        print('j:',j)
        ans+=1

print(ans)