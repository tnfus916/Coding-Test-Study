# def solution(s):
#     cnt = 0
#     idx = -1
#     for x in s:
#         for i in range(len(x)):
#             if x[i] == 1:
#                 if idx == -1:
#                     idx = i
#                 cnt+=1
#             else:
#                 if cnt<=1:
#                     cnt=0
#                     idx=-1
#                 elif cnt==2:
#                     x=x[:idx]+[i-2:i+1]+[1,1,1]+[idx]


#     return
# #

arr = [1, 2, 3, 4, 5, 6]
print(arr[-2:])
