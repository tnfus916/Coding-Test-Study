def get_sum(a,b,type):
    maxsum=0
    for i in range(n):
        for j in range(m):
            if i>=0 and i<n-b+1 and j>=0 and j<m-a+1:
                if type==1: #정사각형
                    maxsum=max(maxsum,board[i][j]+board[i][j+1]+board[i+1][j]+board[i+1][j+1])
                elif type==2: #세로가 긴 직사각형
                    leftsum=board[i][j]+board[i+1][j]+board[i+2][j]
                    rightsum=board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]
                    maxsum=max(maxsum,board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1],board[i][j+1]+board[i+1][j]+board[i+1][j+1]+board[i+2][j],leftsum+board[i][j+1],leftsum+board[i+1][j+1],leftsum+board[i+2][j+1],rightsum+board[i][j],rightsum+board[i+1][j],rightsum+board[i+2][j])
                elif type==3: #가로가 긴 직사각형
                    uppersum=board[i][j]+board[i][j+1]+board[i][j+2]
                    lowersum=board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
                    maxsum=max(maxsum,board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+1][j+2],board[i][j+1]+board[i][j+2]+board[i+1][j]+board[i+1][j+1],uppersum+board[i+1][j],uppersum+board[i+1][j+1],uppersum+board[i+1][j+2],lowersum+board[i][j],lowersum+board[i][j+1],lowersum+board[i][j+2])
                elif type==4:
                    maxsum=max(maxsum,board[i][j]+board[i][j+1]+board[i][j+2]+board[i][j+3])
                elif type==5:
                    maxsum=max(maxsum,board[i][j]+board[i+1][j]+board[i+2][j]+board[i+3][j])
    return maxsum

import sys
input=sys.stdin.readline
n,m=map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]

tet1=get_sum(2,2,1)
tet2=get_sum(2,3,2)
tet3=get_sum(3,2,3)
tet4=get_sum(4,1,4)
tet5=get_sum(1,4,5)
print(max(tet1,tet2,tet3,tet4,tet5))