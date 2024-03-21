def solution(name):
    answer = 0

    move = len(name) - 1

    for idx, n in enumerate(name):
        answer += min(ord(n) - ord("A"), ord("Z") - ord(n) + 1)

        post = idx + 1
        while post < len(name) and name[post] == "A":
            post += 1

        move = min([move, 2 * idx + len(name) - post, idx + 2 * (len(name) - post)])

    answer += move

    return answer
