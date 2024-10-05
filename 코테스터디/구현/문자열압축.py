def solution(s):
    answer = len(s)
    
    if len(s)==1:
        return 1
    
    for leng in range(1,len(s)//2):
        strg=''
        tmp=s[1:leng+1]
        cnt=1
        for i in range(leng+1,len(s)+leng+1,leng):
            if tmp==s[i:i+leng]:
                cnt+=1
            else:
                if cnt!=1:
                    strg=strg+str(cnt)+tmp
                    cnt=1
                else:
                    strg=strg+tmp
                tmp=s[i:i+leng]
                print(strg)
                    
        answer=min(answer,len(strg))
        print(answer)
                    
    return answer

print(solution(input()))