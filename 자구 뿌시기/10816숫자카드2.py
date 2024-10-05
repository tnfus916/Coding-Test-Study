n=int(input())
nlist=list(map(int,input().split()))

m=int(input())
mlist=list(map(int,input().split()))

nlist.sort()

dic={}
for nnum in nlist:
    if nnum not in dic:
        srt=0
        end=n-1
        while srt<=end:
            idx=(srt+end)//2
            if nnum==nlist[idx]:
                dic[nnum]=nlist[srt:end+1].count(nnum)
                break
            elif nnum<nlist[idx]:
                end=idx-1
            else:
                srt=idx+1
for mnum in mlist:
    if mnum in dic:
        print(dic[mnum],end=' ')
    else:
        print(0,end=' ')




