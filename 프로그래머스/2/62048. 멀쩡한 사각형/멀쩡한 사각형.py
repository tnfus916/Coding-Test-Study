import math

def solution(w,h):
    ans = 0
    
    if w<=h:
        x=w
        y=h
    else:
        x=h
        y=w
        
    bottom=0
    for i in range(1,x+1):
        j=y*i/x
        ans+=math.ceil(j)-math.floor(bottom)
        
        if j==int(j):
            ans*=x//i
            break
            
        bottom=j
        
    return w*h-ans