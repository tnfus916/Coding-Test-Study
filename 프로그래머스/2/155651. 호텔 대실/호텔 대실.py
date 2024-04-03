def solution(book_time):
    
    # 모든 시간을 분으로 표시
    book_min=[]
    for s,e in book_time:
        srt_min=int(s[:2])*60+int(s[3:])
        end_min=int(e[:2])*60+int(e[3:])
        book_min.append([srt_min,end_min])
        
    book_min.sort()
    
    time=[] # 대실 종료 시간 저장 
    for srt,end in book_min:
        if len(time)==0:
            time.append(end+10)
            continue
        
        fast_end=min(time)
        if fast_end<=srt:
            time[time.index(fast_end)]=end+10
        else:
            time.append(end+10)
        
    
    return len(time)