def solution(name):
    answer = 0

    min_move = len(name) - 1
    post = 0
    
    for idx, n in enumerate(name):
        answer += min(ord(n) - ord("A"), ord("Z") - ord(n) + 1)

        post = idx + 1
        while post < len(name) and name[post] == "A":
            post += 1

        dist = min(idx, n - post)
        min_move = min(min_move, idx + len(name) - post + dist)

    answer += min_move

    return answer
