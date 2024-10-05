from collections import deque

def solution(number, k):
    answer = ''
    arr=list(map(int,number))
    
    stack=deque([arr[0]])
    top=len(stack)-1
    for i in range(1,len(arr)):
        print(arr[i])
        if k<=0:
            stack.append(arr[i])
            continue
        if stack[top]<arr[i]:
            stack.popleft()
            stack.append(arr[i])
            k-=1
            print(1)
        elif stack[top]==arr[i]:
            stack.append(arr[i])
            top+=1
            print(stack,top)
            print(2)
        else:
            k-=1
            print(3)
            
    answer=''.join(map(str,stack))
    return answer

print(solution("4177252841",4))