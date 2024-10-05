# def check1(d,fromm,zero):
#     global gear

#     # 1번 톱니와 2번 톱니 비교
#     if gear[0][(zero+2)%8]!=gear[1][(zero+6)%8]:
#         if d==1:
#             check2(-1,fromm,(zero+7)%8)
#         else:
#             check2(1,fromm,(zero+1)%8)
#     else:
#         return zero

# def check2(d,fromm,zero):
#     # 2번 톱니와 3번 톱니 비교
#     if fromm=='left':
#         if gear[1][(zero+2)%8]!=gear[2][(zero+6)%8]:
#             if d==1:
#                 check3(-1,fromm,(zero+7)%8)
#             else:
#                 check3(1,fromm,(zero+1)%8)
#     # 1번 톱니와 2번 톱니 비교
#     elif fromm=='right':
#         if gear[0][(zero+2)%8]!=gear[1][(zero+6)%8]:
#             if d==1:

#             else:
#                 check2(1,fromm,(zero+1)%8)
#     else:
#         return zero
#     else:


# input
gear = [list(map(int, " ".join(input()).split(" "))) for _ in range(4)]  # 1 S극
k = int(input())
zero0 = 0
zero1 = 0
zero2 = 0
zero3 = 0
for _ in range(k):
    num, dirc = map(int, input().split())  # 1 시계 방향
    if num == 0:
        # check1(dirc,'left',0)
        if dirc == 1:
            if gear[0][(zero0 + 2) % 8] != gear[1][(zero1 + 6) % 8]:
                if gear[1][(zero1 + 2) % 8] != gear[2][(zero2 + 6) % 8]:
                    if gear[2][(zero2 + 2) % 8] != gear[3][(zero3 + 6) % 8]:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                        zero3 = (zero3 + 7) % 8
                    else:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                else:
                    zero0 = (zero0 + 1) % 8
                    zero1 = (zero1 + 7) % 8
            else:
                zero0 = (zero0 + 1) % 8
        else:
            if gear[0][(zero0 + 2) % 8] != gear[1][(zero1 + 6) % 8]:
                if gear[1][(zero1 + 2) % 8] != gear[2][(zero2 + 6) % 8]:
                    if gear[2][(zero2 + 2) % 8] != gear[3][(zero3 + 6) % 8]:
                        zero0 = (zero0 + 7) % 8
                        zero1 = (zero1 + 1) % 8
                        zero2 = (zero2 + 7) % 8
                        zero3 = (zero3 + 1) % 8
                    else:
                        zero0 = (zero0 + 7) % 8
                        zero1 = (zero1 + 1) % 8
                        zero2 = (zero2 + 7) % 8
                else:
                    zero0 = (zero0 + 7) % 8
                    zero1 = (zero1 + 1) % 8
            else:
                zero0 = (zero0 + 7) % 8
    elif num==1:
        if dirc == 1:
            if gear[0][(zero0 + 2) % 8] != gear[1][(zero1 + 6) % 8]:
                if gear[1][(zero1 + 2) % 8] != gear[2][(zero2 + 6) % 8]:
                    if gear[2][(zero2 + 2) % 8] != gear[3][(zero3 + 6) % 8]:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                        zero3 = (zero3 + 7) % 8
                    else:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                else:
                    zero0 = (zero0 + 1) % 8
                    zero1 = (zero1 + 7) % 8
            else:
                zero0 = (zero0 + 1) % 8
        else:
            if gear[0][(zero0 + 2) % 8] != gear[1][(zero1 + 6) % 8]:
                if gear[1][(zero1 + 2) % 8] != gear[2][(zero2 + 6) % 8]:
                    if gear[2][(zero2 + 2) % 8] != gear[3][(zero3 + 6) % 8]:
                        zero0 = (zero0 + 7) % 8
                        zero1 = (zero1 + 1) % 8
                        zero2 = (zero2 + 7) % 8
                        zero3 = (zero3 + 1) % 8
                    else:
                        zero0 = (zero0 + 7) % 8
                        zero1 = (zero1 + 1) % 8
                        zero2 = (zero2 + 7) % 8
                else:
                    zero0 = (zero0 + 7) % 8
                    zero1 = (zero1 + 1) % 8
            else:
                zero0 = (zero0 + 7) % 8
    elif num==2:
        if dirc == 1:
            if gear[1][(zero1 + 2) % 8] != gear[2][(zero2 + 6) % 8]:
                if gear[2][(zero2 + 2) % 8] != gear[3][(zero3 + 6) % 8]:
                    if gear[0][(zero0 + 2) % 8] != gear[1][(zero1 + 6) % 8]:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                        zero3 = (zero3 + 7) % 8
                    else:
                        zero0 = (zero0 + 1) % 8
                        zero1 = (zero1 + 7) % 8
                        zero2 = (zero2 + 1) % 8
                else:
                    zero1 = (zero1 + 1) % 8
                    zero2 = (zero2 + 7) % 8
            else:
                zero2 = (zero2 + 1) % 8
        else:
            