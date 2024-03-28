def solution(m, musicinfos):
    answer = ''
    
    tmp=[]
    cnt=0
    for info in musicinfos:
        arr=info.split(',')
        
        # 시간 계산 -> 분
        srt_time=list(map(int,arr[0].split(':')))
        end_time=list(map(int,arr[1].split(':')))
        
        time=(end_time[0]*60+end_time[1])-(srt_time[0]*60+srt_time[1])
        
        
        # 악보를 배열로 옮기기
        music=[]
        for i in arr[3]:
            if i=="#":
                music[-1]+="#"
                continue
            music.append(i)
        
        # m을 배열로 옮기기
        memory=[]
        for i in m:
            if i=="#":
                memory[-1]+="#"
                continue
            memory.append(i)
            
        
        # 재생된 음 구하기 
        music_len=len(music)
        if time>music_len:
            play=music*(time//music_len)+music[0:time%music_len]
        elif time<music_len:
            play=music[0:time]
        else:
            play=music
        
        # m이 재생되는 악보에 포함된다면 후보에 추가 
        play_len=len(play)
        m_len=len(memory)
        for i in range(play_len-m_len+1):
            if memory==play[i:i+m_len]:
                tmp.append((time,cnt,arr[2]))
                break 
        
        cnt+=1
    
    if len(tmp)>1:
        tmp.sort(key=lambda x:(-x[0],x[1]))
        return tmp[0][2]
    elif len(tmp)==1:
        return tmp[0][2]
    else:
        return "(None)"
        