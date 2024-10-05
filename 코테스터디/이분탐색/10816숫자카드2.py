import sys
input=sys.stdin.readline

def binary_search(srt,end,num):
    mid=(srt+end)//2
    if num<card[mid]:
        binary_search(srt,mid-1)
    else:
        binary_search(mid,end)

n=int(input())
card=list(map(int,input().split()))
m=int(input())
look=list(map(int,input().split()))

ans=[]
for i in range(m):
    number=look[i]

    # 이분탐색
    card.sort()
    binary_search(0,n-1,number)


        
 