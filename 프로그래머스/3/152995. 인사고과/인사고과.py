def solution(scores):
    wanho = scores[0]
    summ = wanho[0] + wanho[1]

    scores.sort(key=lambda x: (-x[0], x[1]))

    max_peer=0
    result=0
    for att,peer in scores:
        if wanho[0] < att and wanho[1] < peer:
            return -1
        
        if max_peer<=peer:
            max_peer=peer
            if att+peer>summ:
                result+=1
    
    return result +1
