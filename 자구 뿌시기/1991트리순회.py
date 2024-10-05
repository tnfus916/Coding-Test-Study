# def go_right(now):
#     if tree[now]!='.' and tree[now]!=0:
#         print(tree[now])
#         go_right(now)
#     else:
#         return 

# arr=[]
# tree=[0]+['A']+[0]*53

# n=int(input())

# for _ in range(n):
#     arr.append(list(input().split()))
# arr.sort(key=lambda x:x[0])

# for i in range(n):
#     for j in range(2):
#         if arr[i][0]=='A':
#             tree[2]=arr[i][1]
#             tree[3]=arr[i][2]
#             print(tree)
#         else:
#             idx=tree.index(arr[i][0])
#             tree[idx*2]=arr[i][1]
#             tree[idx*2+1]=arr[i][2]

# # 중위 순회 
# for i in range(4,0,-1):
#     if tree[i]!='.' and tree[i]!=0:
#         srt=i
#         break
# print(tree[srt],end='')
# now=srt
# while True:
#     # 부모 노드로 이동
#     now=srt//2
#     print(tree[now])

#     # 오른쪽 자식 노드로 이동
#     now=now*2+1
#     go_right(now)

#     #부모 노드로 이동
#     now=now//2



