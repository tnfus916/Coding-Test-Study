from collections import deque

n=int(input())
board=[[0]*n for _ in range(n)] # 0은 방문x, 1은 방문, 2는 사과
turn=deque([])

apple=int(input())
for _ in range(apple):
    x,y=map(int,input().split())
    board[x][y]=2

switch=int(input())
for _ in range(switch):
    time,rot=map(str,input().split())
    turn.append((int(time),rot))


cur_x,cur_y=0,0
way=[(-1,0),(0,1),(1,0),(0,-1)] #위,오,아래,왼(시계방향)
idx=1
breakchk=0
t=1
board[0][0]=1
while turn:
    time,rot=turn.popleft()
    while t<=time:
        cur_x+=way[idx][0]
        cur_y+=way[idx][1]

        # 방문하지 않았다면 방문 표시, 방문했거나 사과이면 break
        if board[cur_x][cur_y]==0:
            board[cur_x][cur_y]=1
        else:
            breakchk=1
            break

        t+=1
        if t==time:
            if rot=='L':
                idx-=1
            elif rot=='D':
                idx+=1
        break

    if breakchk==1:
        
        break
print(t)



