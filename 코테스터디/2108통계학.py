import sys
input=sys.stdin.readline

n=int(input())
if n>1: # 배열의 개수가 1보다 크면 계산, 1이면 바로 출력
    arr=[]
    cnt={}
    summ=0
    for _ in range(n):
        tmp=int(input())

        arr.append(tmp) # 중앙값과 범위 계산을 위해 arr에 저장
        summ+=tmp   # 산술평균을 계산하기 위한 합구하기

        # 최빈값을 구하기 위해 딕셔너리에 저장
        if tmp in cnt:
            cnt[tmp]+=1
        else:
            cnt[tmp]=1

    arr.sort()  # 정렬 후 중앙값과 범위 계산 

    # 딕셔너리 value값을 기준으로 내림차순 정렬하여 최빈값이 가장 큰 수를 찾고 여러 개일 경우를 위해 key값을 오름차순으로 정렬
    modes=sorted(cnt.items(),key=lambda x:(-x[1],x[0])) 

    if modes[0][1]==modes[1][1]:
        mode=modes[1][0]
    else:
        mode=modes[0][0]

    print(round(summ/n))
    print(arr[n//2])
    print(mode)
    print(arr[n-1]-arr[0])
else: 
    num=int(input())
    print(num)
    print(num)
    print(num)
    print(0)