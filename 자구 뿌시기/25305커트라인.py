N,k=map(int,input().split())
arr=list(map(int,input().split()))


#퀵 정렬
def partition(srt,end):
    if srt>=end:
        return
    pivot=srt
    left=srt+1
    right=end

    while left<=right:
        # arr[pivot]보다 작은 값들은 왼쪽으로 밀어넣겠다.
        while left<=end and arr[left]<=arr[pivot]:
            left+=1
        # arr[pivot]보다 큰 값들은 오른쪽으로 밀어넣겠다.
        while right>srt and arr[right]>=arr[pivot]:
            right-=1
        # 엇갈렸을 때 왼쪽 배열의 끝 인덱스가 right이므로 pivot과 swap
        if left<right:
            arr[right]=arr[right],arr[left]
    print(arr[right],arr[pivot])
    arr[right],arr[pivot]=arr[pivot],arr[right]
    print(arr[pivot],arr[right])

    partition(srt,right-1)
    partition(right+1,end)

    return right

def quick_sort(left,right):
    if left<right:
        pivot=partition(left,right)
        quick_sort(left,pivot-1)
        quick_sort(pivot+1,right)

quick_sort(0,len(arr)-1)
print(arr[N-k])
# # 퀵 정렬
# def partition(srt,end):
#     if srt>=end:
#         return
#     pivot=srt
#     left=srt+1
#     right=end

#     while left<=right:
#         # arr[pivot]보다 작은 값들은 왼쪽으로 밀어넣겠다.
#         print(arr)
#         while left<=end and arr[left]<=arr[pivot]:
#             left+=1
#         # arr[pivot]보다 큰 값들은 오른쪽으로 밀어넣겠다.
#         while right>srt and arr[right]>=arr[pivot]:
#             right-=1
#         # 엇갈렸을 때 왼쪽 배열의 끝 인덱스가 right이므로 pivot과 swap
#         if left<right:
#             arr[right]=arr[right],arr[left]

#     arr[right],arr[pivot]=arr[pivot],arr[right]

#     partition(srt,right-1)
#     partition(right+1,end)

#     return right

# def quick_sort(left,right):
#     if left<right:
#         pivot=partition(left,right)
#         quick_sort(left,pivot-1)
#         quick_sort(pivot+1,right)

# quick_sort(0,len(arr)-1)

# print(arr[k-1])



#셸 정렬
def shell_sort(arr):
    leng=len(arr)
    mid=leng//2
    while mid>0:
        for i in range(mid,leng):
            tmp=arr[i]
            j=i-mid
            while j>=0 and arr[j]>tmp:
                arr[j+mid]=arr[j]
                j-=mid
            arr[j+mid]=tmp
        mid//=2



def merge(arr,srt,mid,end):
    lenn=len(arr)
    tmp=[0]*lenn

    i=srt
    j=mid+1
    k=srt

    while i<=mid and j<=end:
        if arr[i]>=arr[j]:
            tmp[k]=arr[i]
            i+=1
        else:
            tmp[k]=arr[j]
            j+=1
        k+=1
        
    if i>mid:
        for l in range(j,end+1):
            tmp[k]=arr[l]
            k+=1
    else:
        for l in range(i,mid+1):
            tmp[k]=arr[l]
            k+=1

    # print(srt,end)
    # for l in (srt,end):
    #     print(arr,tmp)
    #     arr[l]=tmp[l]
    # print(arr,tmp)
    # 얘 왜 안되는 지 이유 좀?? 

    arr[srt:end+1]=tmp[srt:end+1]


def merge_sort(arr, srt, end):
    if srt<end:
        mid=(srt+end)//2
        merge_sort(arr,srt,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,srt,mid,end)


# merge_sort(arr,0,N-1)


def selection_sort():
    for i in range(N):
        maxx=arr[i]
        idx=i
        for j in range(i+1,N):
            if arr[j]>maxx:
                maxx=arr[j]
                idx=j
        tmp=arr[i]
        arr[i]=maxx
        arr[idx]=tmp

        
def insertion_sort():
    for now in range(1,N):
        while now>0:
            if arr[now-1]>=arr[now]:
                break
            else:
                tmp=arr[now-1]
                arr[now-1]=arr[now]
                arr[now]=tmp
                now-=1
    

def bubble_sort():
    for i in range(N):
        for j in range(N-i-1):
            if arr[j]<arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
            else:
                continue


def merge(arr,srt,mid,end):
    lenn=len(arr)
    tmp=[0]*lenn

    i=srt
    j=mid+1
    k=srt

    while i<=mid and j<=end:
        if arr[i]>=arr[j]:
            tmp[k]=arr[i]
            i+=1
        else:
            tmp[k]=arr[j]
            j+=1
        k+=1
        
    if i>mid:
        for l in range(j,end+1):
            tmp[k]=arr[l]
            k+=1
    else:
        for l in range(i,mid+1):
            tmp[k]=arr[l]
            k+=1

    # print(srt,end)
    # for l in (srt,end):
    #     print(arr,tmp)
    #     arr[l]=tmp[l]
    # print(arr,tmp)
    # 얘 왜 안되는 지 이유 좀?? 

    arr[srt:end+1]=tmp[srt:end+1]


def merge_sort(arr, srt, end):
    if srt<end:
        mid=(srt+end)//2
        merge_sort(arr,srt,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,srt,mid,end)


# merge_sort(arr,0,N-1)


def selection_sort():
    for i in range(N):
        maxx=arr[i]
        idx=i
        for j in range(i+1,N):
            if arr[j]>maxx:
                maxx=arr[j]
                idx=j
        tmp=arr[i]
        arr[i]=maxx
        arr[idx]=tmp

        
def insertion_sort():
    for now in range(1,N):
        while now>0:
            if arr[now-1]>=arr[now]:
                break
            else:
                tmp=arr[now-1]
                arr[now-1]=arr[now]
                arr[now]=tmp
                now-=1
    

def bubble_sort():
    for i in range(N):
        for j in range(N-i-1):
            if arr[j]<arr[j+1]:
                tmp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tmp
            else:
                continue