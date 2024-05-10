from collections import deque

def check(word1,word2):
    cnt=0
    for i in range(len(word1)):
        if word1[i]!=word2[i]:
            cnt+=1
    
    if cnt==1:
        return True
    else:
        return False
        


def solution(begin, target, words):
    if target not in words:
        return 0

    visit = [0] * len(words)
    queue = deque([(begin, 0)])
    while queue:
        now, cnt = queue.popleft()
        if now == target:
            return cnt
    
        for idx, w in enumerate(words):
            if check(now,w) and visit[idx] == 0:
                visit[idx] = 1
                queue.append((w, cnt + 1))
    
    return 0