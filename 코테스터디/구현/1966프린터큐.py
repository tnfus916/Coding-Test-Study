t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split())) # n 크기의 배열

    idx=0
    cnt=0
    maxnum=max(arr)
    while True:
        if len(arr)==0: # 모든 문서가 다 출력되었다면 break
            break

        if arr[idx]>=maxnum: # 현재문서보다 중요한 문서가 없을 때 
            cnt+=1      # 출력 순서 증감
            if idx==m:   # 우리가 찾던 문서가 출력되었을 때
                print(cnt)
                break

            if idx<m: # 출력된 문서의 인덱스가 m보다 작을 때: 다음턴 idx 그대로
                m-=1
                arr.pop(idx)
            elif idx>m:   # 출력된 문서의 인덱스가 m보다 클 때    
                # 다음 반복 턴의 idx 설정(끝값일 때는 맨앞으로, 중간값일 때는 삭제될테니 그대로)
                arr.pop(idx)
                if idx==len(arr)-1: 
                    idx=0
            
            maxnum=max(arr)

        else:
            # 다음턴 idx 설정
            if idx==len(arr)-1: 
                idx=0
            else:
                idx+=1



    
        

    # maxnum=max(arr)
    # cnt=0
    # i=0
    # while True:
    #     print(i)
    #     if arr[i]<maxnum:
    #         arr.append(arr.popleft()) #가장 왼쪽의 값을 뒤에 재배치
    #         if i==m:
    #             m=len(arr)-1
    #         else:
    #             m-=1
    #     else: # 배열의 최대값과 같을 때
    #         cnt+=1
    #         arr.popleft()
    #         if i==m:
    #             print(cnt)
    #             break
    #         else:
    #             m-=1
    #     i+=1







