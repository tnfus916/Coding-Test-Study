import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def find(num):
    if graph[num]==num:
        return num
    graph[num]=find(graph[num])
    return graph[num]

def union(num1,num2):
    num1_group=find(num1)
    num2_group=find(num2)

    if num1_group<num2_group:
        graph[num2_group]=num1_group
    elif num1_group>num2_group:
        graph[num1_group]=num2_group
    else:
        return 

n,m=map(int,input().split())

graph=[i for i in range(n+2)]
for _ in range(m):
    cal,a,b=map(int,input().split())
    if cal==0:
        union(a,b)
    elif cal==1:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')

