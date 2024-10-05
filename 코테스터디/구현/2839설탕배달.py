n=int(input())

breakcheck=0
for i in range(n//5,-1,-1):
    if (n-5*i)%3==0:
        five=i
        three=(n-5*i)//3
        breakcheck=1
        break

if breakcheck==1:
    print(five+three)
else:
    print(-1)


