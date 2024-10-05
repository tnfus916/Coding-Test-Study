def del_mid(arr):
    leng=len(arr)
    if leng==1:
        return arr
    unit=leng//3
    side=[1]*unit
    middle=[0]*unit
    return del_mid(side)+middle+del_mid(side)

while True:
    try:
        n=int(input())
        num=3**n
        arr=[1]*num
        ans=del_mid(arr)
        for a in ans:
            if a==1:
                print('-',end='')
            else:
                print(' ',end='')
        print()
    except EOFError:
        break