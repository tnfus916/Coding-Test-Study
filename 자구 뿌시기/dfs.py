def dfs(idx,summ):
    global answer
    print(idx,summ)
    if idx==len(numbers)-1:
        if summ==target:
            answer+=1
        return

    dfs(idx+1,summ+numbers[idx+1])
    dfs(idx+1,summ-numbers[idx+1])
    return answer   

numbers=list(map(int,input().split()))
target=int(input())

answer = 0
dfs(-1,0)

print(answer)

