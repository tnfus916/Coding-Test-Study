import sys
input=sys.stdin.readline

n=int(input()) # 회의의 수 
timetable=[] # 회의의 시작시간과 끝나는 시간을 저장할 리스트
for _ in range(n):
    srt,end=map(int,input().split())
    timetable.append((srt,end))

# 끝나는 시간을 기준으로 정렬
timetable.sort(key=lambda x:(x[1],x[0]))


end=timetable[0][1] # 가장 일찍 끝나는 회의의 끝시간을 end에 저장
cnt=1 # end에 저장한 회의 카운트 

# 두번째 회의부터 카운트 시작
for i in range(1,n): 
    if timetable[i][0]>=end: # 시작시간이 이전 회의의 끝시간보다 뒤에 있다면 cnt+=1
        cnt+=1
        end=timetable[i][1] # end에, 선택한 회의의 끝시간 저장

print(cnt)