import sys
from math import sqrt
input=sys.stdin.readline

# 에라토스테네스의 체
maxn=10**6
prime=[False,False]+[True]*(maxn+1)
for i in range(2,maxn+1):
    if prime[i]==True:
        for j in range(i*2,maxn+1,i):
            prime[j]=False

while True:
    # 입력
    n=int(input())
    if n==0: break
    break_check=False
    for a in range(3, n//2+1,2):
        if prime[a]==True and prime[n-a]==True:
            print(f'{n} = {a} + {n-a}')
            break_check=True
            break
    if break_check==False:
        print("Goldbach's conjecture is wrong.")
