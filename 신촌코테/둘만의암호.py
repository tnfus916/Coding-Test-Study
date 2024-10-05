def solution(s, skip, index):
    answer = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in s:
        idx = alphabet.index(letter)

        i, cnt = 1, 1
        while cnt <= index:
            if alphabet[(idx + i) % 26] in skip:
                i += 1
                continue

            cnt += 1
            i += 1

        answer += alphabet[(idx + i - 1) % 26]

    return answer
